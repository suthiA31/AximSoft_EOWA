from tensorflow.keras.models import load_model
from gradcam import generate_gradcam
from prediction import predict_image
from disease_info import DISEASE_INFO


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

CLASS_NAMES = [
    "Actinic Keratosis",
    "Basal Cell Carcinoma",
    "Benign Keratosis",
    "Dermatofibroma",
    "Melanocytic Nevus",
    "Melanoma",
    "Vascular Lesion"
]

# =====================================================
# Helper Function
# =====================================================

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

            gradcam_image = generate_gradcam(filepath)

            disease_details = DISEASE_INFO[prediction]
            report_path = create_diagnosis_report(

                uploaded_image=filepath,

                gradcam_image=gradcam_image,

                prediction=prediction,

                confidence=confidence,

                probabilities=probabilities,

                disease_details=disease_details

            )
            return render_template(
                "predict.html",
                uploaded_image=filepath,
                prediction=prediction,
                confidence=confidence,
                probabilities=probabilities,
                gradcam_image=gradcam_image,
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