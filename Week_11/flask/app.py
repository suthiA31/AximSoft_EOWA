from flask import (
    Flask,
    render_template,
    request,
    send_file,
    redirect,
    url_for
)

import os
import pickle
import pandas as pd
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

from wordcloud import WordCloud


# ---------------------------------------------------
# Flask Configuration
# ---------------------------------------------------

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "uploads"

os.makedirs(
    app.config["UPLOAD_FOLDER"],
    exist_ok=True
)


# ---------------------------------------------------
# Model Configuration
# ---------------------------------------------------

MODEL_PATH = "models/optimized_BiLSTM.keras"

TOKENIZER_PATH = "processing/tokenizer.pkl"

DATASET_PATH = "processing/imdb_cleaned.csv"

MAX_LENGTH = 200


# ---------------------------------------------------
# Load Model
# ---------------------------------------------------

print("Loading Bi-LSTM model...")

model = load_model(
    MODEL_PATH
)

print("Bi-LSTM model loaded successfully!")


# ---------------------------------------------------
# Load Tokenizer
# ---------------------------------------------------

with open(
    TOKENIZER_PATH,
    "rb"
) as file:

    tokenizer = pickle.load(file)


print("Tokenizer loaded successfully!")


# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

try:

    df = pd.read_csv(
        DATASET_PATH
    )

except Exception:

    df = pd.DataFrame(
        columns=[
            "review",
            "sentiment"
        ]
    )


# ---------------------------------------------------
# Dashboard Statistics
# ---------------------------------------------------

total_reviews = len(df)

positive_reviews = 0

negative_reviews = 0

if "sentiment" in df.columns:

    positive_reviews = int(
        (
            df["sentiment"]
            .astype(str)
            .str.lower()
            == "positive"
        ).sum()
    )

    negative_reviews = int(
        (
            df["sentiment"]
            .astype(str)
            .str.lower()
            == "negative"
        ).sum()
    )


# ---------------------------------------------------
# Load Comparison Files
# ---------------------------------------------------

def load_csv_file(filename):

    path = os.path.join(
        "uploads",
        filename
    )

    if os.path.exists(path):

        try:

            return pd.read_csv(path)

        except Exception:

            return pd.DataFrame()

    return pd.DataFrame()


baseline_df = load_csv_file(
    "model_comparison.csv"
)

optimized_df = load_csv_file(
    "final_model_comparison.csv"
)


# ---------------------------------------------------
# Prediction Function
# ---------------------------------------------------

def predict_sentiment(review):

    sequence = tokenizer.texts_to_sequences(
        [review]
    )

    padded = pad_sequences(
        sequence,
        maxlen=MAX_LENGTH,
        padding="post",
        truncating="post"
    )

    probability = float(
        model.predict(
            padded,
            verbose=0
        )[0][0]
    )

    positive_probability = probability

    negative_probability = 1 - probability

    if probability >= 0.5:

        sentiment = "Positive"

        confidence = positive_probability

    else:

        sentiment = "Negative"

        confidence = negative_probability


    return {
        "sentiment": sentiment,
        "confidence": confidence * 100,
        "positive": positive_probability * 100,
        "negative": negative_probability * 100
    }


# ---------------------------------------------------
# HOME DASHBOARD
# ---------------------------------------------------

@app.route("/")
def index():

    return render_template(
        "index.html",

        total_reviews=total_reviews,

        positive_reviews=positive_reviews,

        negative_reviews=negative_reviews,

        best_model="Bi-LSTM",

        model_accuracy="Best Model",

        optimized_data=optimized_df.to_dict(
            orient="records"
        )
    )


# ---------------------------------------------------
# SENTIMENT PREDICTION
# ---------------------------------------------------

@app.route(
    "/predict",
    methods=["GET", "POST"]
)
def predict():

    result = None

    review = ""

    if request.method == "POST":

        review = request.form.get(
            "review",
            ""
        )

        if review.strip():

            result = predict_sentiment(
                review
            )


    return render_template(
        "predict.html",
        result=result,
        review=review
    )


# ---------------------------------------------------
# MODEL COMPARISON
# ---------------------------------------------------

@app.route("/comparison")
def comparison():

    baseline_records = (
        baseline_df.to_dict(
            orient="records"
        )
    )

    optimized_records = (
        optimized_df.to_dict(
            orient="records"
        )
    )

    return render_template(
        "comparison.html",

        baseline=baseline_records,

        optimized=optimized_records
    )


# ---------------------------------------------------
# TEXT ANALYTICS
# ---------------------------------------------------

@app.route("/analytics")
def analytics():

    return render_template(
        "analytics.html"
    )

# ---------------------------------------------------
# BATCH PREDICTION
# ---------------------------------------------------

@app.route(
    "/batch",
    methods=["GET", "POST"]
)
def batch():

    results = None

    filename = None

    if request.method == "POST":

        file = request.files.get(
            "file"
        )

        if file and file.filename:

            filename = file.filename

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                filename
            )

            file.save(
                filepath
            )

            uploaded_df = pd.read_csv(
                filepath
            )

            if "review" not in uploaded_df.columns:

                return render_template(
                    "batch.html",
                    error=(
                        "CSV must contain a "
                        "'review' column."
                    )
                )


            predictions = []

            confidences = []

            for review in uploaded_df["review"]:

                result = predict_sentiment(
                    str(review)
                )

                predictions.append(
                    result["sentiment"]
                )

                confidences.append(
                    result["confidence"]
                )


            uploaded_df[
                "Predicted Sentiment"
            ] = predictions

            uploaded_df[
                "Confidence"
            ] = np.round(
                confidences,
                2
            )


            output_path = os.path.join(
                app.config["UPLOAD_FOLDER"],
                "sentiment_predictions.csv"
            )

            uploaded_df.to_csv(
                output_path,
                index=False
            )


            results = uploaded_df.head(
                20
            ).to_dict(
                orient="records"
            )


    return render_template(
        "batch.html",

        results=results,

        filename=filename
    )


# ---------------------------------------------------
# DOWNLOAD BATCH RESULTS
# ---------------------------------------------------

@app.route(
    "/download"
)
def download():

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        "sentiment_predictions.csv"
    )

    if os.path.exists(filepath):

        return send_file(
            filepath,
            as_attachment=True,
            download_name=(
                "sentiment_predictions.csv"
            )
        )

    return redirect(
        url_for("batch")
    )


# ---------------------------------------------------
# RUN APPLICATION
# ---------------------------------------------------

if __name__ == "__main__":

    app.run(
        debug=True
    )