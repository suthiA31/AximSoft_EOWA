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

def preprocess_image(image_path):
    """
    Load and preprocess image for prediction.
    """

    image = Image.open(image_path).convert("RGB")

    image = image.resize(IMG_SIZE)

    image = np.array(image)

    image = image.astype("float32") / 255.0

    image = np.expand_dims(image, axis=0)

    return image


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