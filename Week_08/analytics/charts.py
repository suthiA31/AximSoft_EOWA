import joblib
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots


model = joblib.load("/home/aximsoft/Documents/EOWA/Week_08/Notebooks/dataset/models/best_model.pkl")
def layout(fig,title):

    fig.update_layout(

        title=title,

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(color="white"),

        margin=dict(l=20,r=20,t=50,b=20),

        height=430

    )

    return fig.to_html(full_html=False)
def saleprice_chart(df):

    fig=px.histogram(

        df,

        x="SalePrice",

        nbins=40,

        color_discrete_sequence=["#A855F7"]

    )

    return layout(fig,"Sale Price Distribution")
def feature_chart():

    features=[

        "OverallQual",

        "GrLivArea",

        "GarageCars",

        "TotalBsmtSF",

        "FullBath",

        "YearBuilt"

    ]

    importance=pd.Series(

        model.feature_importances_,

        index=features

    ).sort_values()

    fig=px.bar(

        importance,

        orientation="h",

        color_discrete_sequence=["#C084FC"]

    )

    return layout(fig,"Feature Importance")
def comparison_chart(comparison):

    fig=px.bar(

        comparison,

        x="Model",

        y="R2 Score",

        color="Model"

    )

    return layout(fig,"Regression Model Comparison")
def heatmap_chart(df):

    corr = df.select_dtypes(include="number").corr()

    fig = px.imshow(

        corr,

        text_auto=".2f",

        color_continuous_scale="Purples",

        aspect="auto"

    )

    return layout(fig, "Correlation Heatmap")
def actual_predicted_chart(y_test, prediction):

    fig = px.scatter(

        x=y_test,

        y=prediction,

        labels={

            "x": "Actual Price",

            "y": "Predicted Price"

        },

        color_discrete_sequence=["#A855F7"]

    )

    fig.add_shape(

        type="line",

        x0=min(y_test),

        y0=min(y_test),

        x1=max(y_test),

        y1=max(y_test),

        line=dict(color="white", dash="dash")

    )

    return layout(fig, "Actual vs Predicted")
def residual_chart(y_test, prediction):

    residuals = y_test - prediction

    fig = px.scatter(

        x=prediction,

        y=residuals,

        labels={

            "x": "Predicted",

            "y": "Residual"

        },

        color_discrete_sequence=["#C084FC"]

    )

    fig.add_hline(

        y=0,

        line_dash="dash",

        line_color="white"

    )

    return layout(fig, "Residual Plot")
def quality_chart(df):

    data = (

        df.groupby("OverallQual")
        .size()
        .reset_index(name="Count")

    )


    fig = px.bar(

        data,

        x="OverallQual",

        y="Count",

        color_discrete_sequence=["#7C3AED"]

    )


    return layout(

        fig,

        "Overall Quality Distribution"

    )

def living_chart(df):

    fig = px.scatter(

        df,

        x="GrLivArea",

        y="SalePrice",

        color="OverallQual",

        color_continuous_scale="Purples"

    )


    return layout(

        fig,

        "Living Area vs Sale Price"

    )
