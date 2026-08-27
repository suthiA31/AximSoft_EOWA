import tensorflow as tf
import keras

print("TensorFlow:", tf.__version__)
print("Keras:", keras.__version__)

print("Loading model...")

model = keras.saving.load_model(
    "models/optimized_BiLSTM.keras",
    compile=False
)

print("MODEL LOADED SUCCESSFULLY!")

model.summary()