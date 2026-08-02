import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model, Model

# =====================================================
# Load Model
# =====================================================

MODEL_PATH = "model/resnetmodel_Lr.keras"

model = load_model(MODEL_PATH)

# =====================================================
# Configuration
# =====================================================

IMG_SIZE = (128, 128)

OUTPUT_FOLDER = "static/gradcam"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# =====================================================
# Get ResNet50 Base Model
# =====================================================

base_model = model.get_layer("resnet50")

last_conv_layer = base_model.get_layer("conv5_block3_out")

# =====================================================
# Preprocess Image
# =====================================================

def preprocess_image(image_path):

    image = tf.keras.preprocessing.image.load_img(
        image_path,
        target_size=IMG_SIZE
    )

    image = tf.keras.preprocessing.image.img_to_array(image)

    image = image.astype("float32") / 255.0

    image = np.expand_dims(image, axis=0)

    return image


# =====================================================
# Generate Grad-CAM
# =====================================================

def generate_gradcam(image_path):

    image = preprocess_image(image_path)

    # Forward through classifier head
    x = base_model.output

    x = model.get_layer("global_average_pooling2d_1")(x)

    x = model.get_layer("dense_2")(x)

    x = model.get_layer("dropout_1")(x)

    predictions = model.get_layer("dense_3")(x)

    grad_model = Model(
        inputs=base_model.input,
        outputs=[
            last_conv_layer.output,
            predictions
        ]
    )

    with tf.GradientTape() as tape:

        conv_outputs, predictions = grad_model(image)

        class_index = tf.argmax(predictions[0])

        loss = predictions[:, class_index]

    gradients = tape.gradient(loss, conv_outputs)

    if gradients is None:
        raise Exception("Gradients are None.")

    pooled_gradients = tf.reduce_mean(
        gradients,
        axis=(0, 1, 2)
    )

    conv_outputs = conv_outputs[0]

    heatmap = tf.reduce_sum(
        conv_outputs * pooled_gradients,
        axis=-1
    )

    heatmap = tf.maximum(heatmap, 0)

    heatmap = heatmap / (tf.reduce_max(heatmap) + 1e-8)

    heatmap = heatmap.numpy()

    # =====================================================
    # Overlay Heatmap
    # =====================================================

    original = cv2.imread(image_path)

    original = cv2.resize(original, IMG_SIZE)

    heatmap = cv2.resize(heatmap, IMG_SIZE)

    heatmap = np.uint8(255 * heatmap)

    heatmap = cv2.applyColorMap(
        heatmap,
        cv2.COLORMAP_JET
    )

    superimposed = cv2.addWeighted(
        original,
        0.6,
        heatmap,
        0.4,
        0
    )

    save_path = os.path.join(
        OUTPUT_FOLDER,
        "gradcam.png"
    )

    cv2.imwrite(save_path, superimposed)

    return save_path