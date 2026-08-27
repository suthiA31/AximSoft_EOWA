import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Input,
    Embedding,
    Bidirectional,
    LSTM,
    Dense,
    Dropout
)

print("TensorFlow:", tf.__version__)
print("Building Bi-LSTM architecture...")

model = Sequential([

    Input(shape=(200,)),

    Embedding(
        input_dim=20000,
        output_dim=128
    ),

    Bidirectional(
        LSTM(
            64,
            dropout=0.3,
            recurrent_dropout=0.2
        )
    ),

    Dense(
        32,
        activation="relu"
    ),

    Dropout(0.3),

    Dense(
        1,
        activation="sigmoid"
    )
])

print()
print("Architecture created successfully!")
print()

model.summary()

print()
print("Loading trained weights...")

model.load_weights(
    "models/optimized_BiLSTM.keras",
    by_name=False
)