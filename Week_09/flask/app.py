from tensorflow.keras.models import load_model

from prediction import predict_image
from disease_info import DISEASE_INFO

import cv2
import matplotlib
from tensorflow.keras.preprocessing import image
import os
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)
from werkzeug.utils import secure_filename

# =====================================================
# Flask Configuration
# =====================================================

app = Flask(__name__)

app.secret_key = "skin_disease_secret"

UPLOAD_FOLDER = "static/uploads"

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# =====================================================
# Class Names
# =====================================================




# =====================================================
# Helper Function
# =====================================================
import numpy as np
import tensorflow as tf
from PIL import Image
import keras
# ============================================
# Load Model
# ============================================

MODEL_PATH = "model/resnet_SGD.keras"
model= keras.models.load_model(MODEL_PATH)

# ============================================
# Class Names
# ============================================

CLASS_NAMES = [
    "Actinic Keratosis",      # 0
    "Basal Cell Carcinoma",   # 1
    "Benign Keratosis",       # 2
    "Dermatofibroma",         # 3
    "Melanoma",               # 4
    "Melanocytic Nevus",      # 5
    "Vascular Lesion"         # 6
]

# ============================================
# Image Size
# ============================================

IMG_SIZE = (224, 224)

# ============================================
# Preprocess Image
# ============================================

from tensorflow.keras.applications.resnet50 import preprocess_input

def preprocess_image(image_path):

    image = Image.open(image_path).convert("RGB")

    image = image.resize(IMG_SIZE)

    image = np.array(image)

    image = preprocess_input(image)

    image = np.expand_dims(image, axis=0)

    return image





def make_gradcam_heatmap(img_array, model, last_conv_layer_name):
    grad_model = tf.keras.models.Model(
        inputs=model.inputs,
        outputs=[
            model.get_layer(last_conv_layer_name).output,
            model.output
        ]
    )

    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img_array)
        pred_index = tf.argmax(predictions[0])
        class_channel = predictions[:, pred_index]

    grads = tape.gradient(class_channel, conv_outputs)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    conv_outputs = conv_outputs[0]
    heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)
    heatmap = tf.maximum(heatmap, 0)
    max_val = tf.reduce_max(heatmap)

    if max_val != 0:
        heatmap /= max_val

    return heatmap.numpy()


# save the cam
def save_gradcam(img_path):
    print("save_gradcam() called")

    img = image.load_img(img_path, target_size=(224, 224))
    from tensorflow.keras.applications.resnet50 import preprocess_input

    img_array = image.img_to_array(img)
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)

    heatmap = make_gradcam_heatmap(
        img_array,
        model,
        "conv5_block3_out"
    )

    print("Heatmap Shape:", heatmap.shape)
    img = cv2.imread(img_path)
    print("Original Image:", img.shape)

    img = cv2.resize(img, (224, 224))
    heatmap = np.uint8(255 * heatmap)
    print("Heatmap Converted:", heatmap.shape)

    jet = matplotlib.colormaps["jet"]
    jet_colors = jet(np.arange(256))[:, :3]
    jet_heatmap = jet_colors[heatmap]
    jet_heatmap = cv2.resize(jet_heatmap, (224, 224))
    jet_heatmap = np.uint8(jet_heatmap * 255)

    overlay = cv2.addWeighted(img, 0.6, jet_heatmap, 0.4, 0)
    output_path = os.path.join(
        "static",
        "uploads",
        "gradcam_overlay.jpg"
    )

    print("Saving:", output_path)
    cv2.imwrite(output_path, overlay)
    print("Saved:", os.path.exists(output_path))

    return "uploads/gradcam_overlay.jpg"


# ============================================
# Predict Disease
# ============================================

def predict_image(image_path):
    """
    Predict disease from image.
    """

    image = preprocess_image(image_path)

    predictions = model.predict(image, verbose=0)

    print("\n========== Prediction ==========")
    print(predictions[0])
    print("Predicted Index:", np.argmax(predictions[0]))
    print("================================\n")

    probabilities = predictions[0]

    predicted_index = np.argmax(probabilities)

    predicted_class = CLASS_NAMES[predicted_index]

    confidence = float(probabilities[predicted_index] * 100)

    probability_dict = {}

    for disease, probability in zip(CLASS_NAMES, probabilities):
        probability_dict[disease] = round(float(probability * 100), 2)

    return (
        predicted_class,
        round(confidence, 2),
        probability_dict
    )
def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

# =====================================================
# Home
# =====================================================

@app.route("/")
def home():

    return render_template("index.html")

# =====================================================
# Dashboard
# =====================================================

@app.route("/dashboard")
def dashboard():

    return render_template("dashboard.html")

# =====================================================
# Prediction
# =====================================================

@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        if "image" not in request.files:
            flash("Please upload an image.")
            return redirect(request.url)

        image = request.files["image"]

        if image.filename == "":
            flash("No image selected.")
            return redirect(request.url)

        if image and allowed_file(image.filename):

            filename = secure_filename(image.filename)

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                filename
            )

            image.save(filepath)

            prediction, confidence, probabilities = predict_image(filepath)
            gradcam_image = save_gradcam(filepath)

            disease_details = DISEASE_INFO[prediction]
            report_path = create_diagnosis_report(
                uploaded_image=filepath,

                prediction=prediction,
                confidence=confidence,
                probabilities=probabilities,
                disease_details=disease_details
            )
            return render_template(
                "predict.html",
                uploaded_image=filepath,
                gradcam_image="static/uploads/gradcam_overlay.jpg",
                prediction=prediction,
                confidence=confidence,
                probabilities=probabilities,
                disease_details=disease_details
            )
    return render_template("predict.html")

# =====================================================
# Analytics
# =====================================================

@app.route("/analytics")
def analytics():

    return render_template("analytics.html")

# =====================================================
# Reports
# =====================================================

@app.route("/reports")
def reports():

    return render_template("reports.html")

# =====================================================
# Model Comparison
# =====================================================

@app.route("/comparison")
def comparison():

    return render_template("comparison.html")

# =====================================================
# About
# =====================================================

@app.route("/about")
def about():

    return render_template("about.html")

# =====================================================
# Main
# =====================================================
from flask import send_from_directory
from diagnosis import create_diagnosis_report
@app.route("/download_diagnosis")
def download_diagnosis():
    return send_from_directory(
        "reports",
        "Diagnosis_Report.pdf",
        as_attachment=True
    )
@app.route("/download_preprocess")
def download_pre():
    return send_from_directory(
        "reports",
        "Data_Preprocessing_Report.pdf",
        as_attachment=True
    )
@app.route("/download_modeltraing")
def download_dimodeltraing():
    return send_from_directory(
        "reports",
        "Model_Training_Report.pdf",
        as_attachment=True
    )
@app.route("/download_explainAi")
def download_explainAi():
    return send_from_directory(
        "reports",
        "Explainable_AI_Report.pdf",
        as_attachment=True
    )
@app.route("/download_comparison")
def download_comparison():
    return send_from_directory(
        "reports",
        "Model_Comparison_Report.pdf",
        as_attachment=True
    )

@app.route("/download_evaluation")
def download_evaluation():
    return send_from_directory(
        "reports",
        "Model_Evaluation_Report.pdf",
        as_attachment=True
    )
if __name__ == "__main__":

    app.run(
        debug=True
    )