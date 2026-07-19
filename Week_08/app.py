from flask import Flask
from flask import render_template
from flask import request

import joblib
import numpy as np

from analytics.data_loader import load_data
from analytics.data_loader import load_comparison

from analytics.kpi import get_dashboard_kpis

from analytics.charts import saleprice_chart
from analytics.charts import *
from analytics.charts import feature_chart
from analytics.charts import comparison_chart
from analytics.charts import heatmap_chart
from flask import send_file

app = Flask(__name__)


# -------------------------------------------------

# Load Dataset

# -------------------------------------------------

df = load_data()

comparison = load_comparison()

model = joblib.load("/home/aximsoft/Documents/EOWA/Week_08/Notebooks/dataset/models/best_model.pkl")


# -------------------------------------------------

# Dashboard

# -------------------------------------------------

@app.route("/")
def dashboard():

    df = load_data()

    comparison_df = load_comparison()

    kpis = get_dashboard_kpis(

        df,

        comparison_df

    )

    return render_template(

        "dashboard.html",

        kpi=kpis,

        sale_chart=saleprice_chart(df),

        quality_chart=quality_chart(df),

        living_chart=living_chart(df),

        feature_chart=feature_chart(),

        comparison_chart=comparison_chart(comparison_df)

    )


# -------------------------------------------------

# Prediction Page

# -------------------------------------------------

@app.route("/prediction")

def prediction():

    return render_template(

        "prediction.html"

    )


# -------------------------------------------------

# Predict

# -------------------------------------------------

@app.route(

    "/predict",

    methods=["POST"]

)

def predict():

    values = np.array([[

        float(request.form["OverallQual"]),

        float(request.form["GrLivArea"]),

        float(request.form["GarageCars"]),

        float(request.form["TotalBsmtSF"]),

        float(request.form["FullBath"]),

        float(request.form["YearBuilt"])

    ]])

    prediction = model.predict(values)[0]

    return render_template(

        "prediction.html",

        prediction=round(prediction,2)

    )


# -------------------------------------------------

# Analytics

# -------------------------------------------------
@app.route("/analytics")
def analytics():

    df = load_data()

    return render_template(

        "analytics.html",

        sale_chart=saleprice_chart(df),

        quality_chart=quality_chart(df),

        living_chart=living_chart(df),

        feature_chart=feature_chart(),

        heatmap_chart=heatmap_chart(df)

    )


# -------------------------------------------------

# Comparison

# -------------------------------------------------

@app.route("/comparison")
def comparison():

    comparison_df = load_comparison()

    return render_template(

        "comparison.html",

        comparison=comparison_df,

        comparison_chart=comparison_chart(comparison_df)

    )


# -------------------------------------------------

# Reports

# -------------------------------------------------

@app.route("/reports")

def reports():

    return render_template(

        "reports.html"

    )
@app.route("/download/evaluation")
def evaluation_report():

    return send_file(

        "/home/aximsoft/Documents/EOWA/Week_08/Notebooks/dataset/reports/model_evaluation.pdf",

        as_attachment=True

    )


@app.route("/download/comparison")
def comparison_report():

    return send_file(

        "/home/aximsoft/Documents/EOWA/Week_08/Notebooks/dataset/reports/model_comparison.pdf",

        as_attachment=True

    )


@app.route("/download/model")
def model_report():

    return send_file(

        "/home/aximsoft/Documents/EOWA/Week_08/Notebooks/dataset/reports/model_interpretation.pdf",

        as_attachment=True

    )


# -------------------------------------------------

# Run

# -------------------------------------------------

if __name__ == "__main__":

    app.run(

        debug=True

    )