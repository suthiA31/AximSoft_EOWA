from flask import Flask, render_template
import pandas as pd
import numpy as np
import tensorflow as tf
import joblib


app = Flask(__name__)


# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv(
    "/home/aximsoft/Documents/AximSoft_EOWA/Week_10/dataset/pjm_processed.csv",
    parse_dates=["timestamp"]
)

df = df.sort_values("timestamp")
df = df.reset_index(drop=True)


# -----------------------------
# Load Model
# -----------------------------

model = tf.keras.models.load_model(
    "/home/aximsoft/Documents/AximSoft_EOWA/Week_10/final_gru_forecasting_model11.keras"
)


# -----------------------------
# Load Scalers
# -----------------------------

feature_scaler = joblib.load(
    "/home/aximsoft/Documents/AximSoft_EOWA/Week_10/feature_scaler.pkl"
)

target_scaler = joblib.load(
    "/home/aximsoft/Documents/AximSoft_EOWA/Week_10/target_scaler.pkl"
)


# -----------------------------
# Features
# -----------------------------

features = [
    "demand",
    "lag_1",
    "lag_24",
    "lag_48",
    "lag_168",
    "rolling_mean_24",
    "rolling_std_24",
    "rolling_mean_168",
    "rolling_std_168"
]


# -----------------------------
# Forecast Function
# -----------------------------

def generate_forecast():

    latest_data = df.tail(168)

    X = latest_data[features]

    X_scaled = feature_scaler.transform(X)

    X_scaled = X_scaled.reshape(
        1,
        168,
        len(features)
    )

    prediction = model.predict(
        X_scaled,
        verbose=0
    )

    prediction = prediction.reshape(
        -1,
        1
    )

    prediction = target_scaler.inverse_transform(
        prediction
    )

    prediction = prediction.flatten()

    last_timestamp = df["timestamp"].iloc[-1]

    future_timestamps = pd.date_range(
        start=last_timestamp + pd.Timedelta(hours=1),
        periods=24,
        freq="h"
    )

    forecast = pd.DataFrame({
        "timestamp": future_timestamps,
        "demand": prediction
    })

    return forecast




@app.route("/forecast")
def forecast():

    forecast_df = generate_forecast()

    forecast_data = forecast_df.to_dict(
        orient="records"
    )

    return render_template(
        "forecast.html",
        forecast=forecast_data
    )





@app.route("/")
def dashboard():
    return render_template("dashboard.html")





@app.route("/analytics")
def analytics():
    return render_template("analytics.html")


@app.route("/validation")
def validation():
    return render_template("validation.html")


if __name__ == "__main__":
    app.run(debug=True)