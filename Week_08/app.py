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

model = joblib.load("/home/aximsoft/Documents/AximSoft_EOWA/Week_08/Notebooks/dataset/models/best_model1.pkl")



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

        kpi=kpis

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
        float(request.form["YearBuilt"]),
        float(request.form["1stFlrSF"]),
        float(request.form["TotRmsAbvGrd"]),
        float(request.form["Fireplaces"]),
        float(request.form["LotArea"])
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



    return render_template(

        "analytics.html",



    )


# -------------------------------------------------

# Comparison

# -------------------------------------------------

@app.route("/comparison")
def comparison():



    return render_template(

        "comparison.html",

        comparison=comparison_df,


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

        "/home/aximsoft/Documents/AximSoft_EOWA//Week_08/Notebooks/dataset/reports/model_evaluation.pdf",

        as_attachment=True

    )


@app.route("/download/comparison")
def comparison_report():

    return send_file(

        "/home/aximsoft/Documents/AximSoft_EOWA//Week_08/Notebooks/dataset/reports/model_comparison.pdf",

        as_attachment=True

    )


@app.route("/download/model")
def model_report():

    return send_file(

        "/home/aximsoft/Documents/AximSoft_EOWA//Week_08/Notebooks/dataset/reports/model_interpretation.pdf",

        as_attachment=True

    )
@app.route("/download/EDA")
def eda_report():

    return send_file(

        "/home/aximsoft/Documents/AximSoft_EOWA//Week_08/Notebooks/dataset/reports/eda_report.pdf",

        as_attachment=True

    )
@app.route("/download/Preprocessing")
def Preprocessing_report():

    return send_file(

        "/home/aximsoft/Documents/AximSoft_EOWA//Week_08/Notebooks/dataset/reports/preprocessing_report.pdf",

        as_attachment=True

    )


# -------------------------------------------------

# Run

# -------------------------------------------------

if __name__ == "__main__":

    app.run(

        debug=True

    )