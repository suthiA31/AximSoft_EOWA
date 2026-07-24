from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

styles = getSampleStyleSheet()

doc = SimpleDocTemplate("/home/aximsoft/Documents/AximSoft_EOWA/Week_08/Notebooks/dataset/reports/eda_report.pdf")

story = []

# --------------------------------------------------
# Title
# --------------------------------------------------

story.append(
    Paragraph(
        "<b>EXPLORATORY DATA ANALYSIS (EDA) REPORT</b>",
        styles["Title"]
    )
)

story.append(Spacer(1, 20))

story.append(
    Paragraph(
        "Project : Advanced Regression Model Comparison & Optimization Platform",
        styles["Heading2"]
    )
)

story.append(
    Paragraph(
        "Dataset : House Prices - Advanced Regression Techniques",
        styles["Normal"]
    )
)

story.append(Spacer(1, 20))

# --------------------------------------------------
# Project Objective
# --------------------------------------------------

story.append(
    Paragraph(
        "<b>1. Business Objective</b>",
        styles["Heading2"]
    )
)

story.append(
    Paragraph(
        """
        The objective of this project is to analyze housing data,
        identify the factors affecting house prices and understand
        the relationships between different property features before
        building regression models. Exploratory Data Analysis helps
        discover data quality issues, feature distributions, missing
        values and correlations that influence prediction accuracy.
        """,
        styles["BodyText"]
    )
)

story.append(Spacer(1, 20))

# --------------------------------------------------
# Dataset Summary
# --------------------------------------------------

story.append(
    Paragraph(
        "<b>2. Dataset Summary</b>",
        styles["Heading2"]
    )
)

summary = [

    ["Attribute", "Value"],

    ["Dataset", "House Prices"],

    ["Total Records", "1460"],

    ["Total Features", "80"],

    ["Target Variable", "SalePrice"],

    ["Numerical Features", "37"],

    ["Categorical Features", "43"]

]

table = Table(summary)

table.setStyle(TableStyle([

    ("BACKGROUND",(0,0),(-1,0),colors.darkblue),

    ("TEXTCOLOR",(0,0),(-1,0),colors.white),

    ("GRID",(0,0),(-1,-1),1,colors.black),

    ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),

    ("ALIGN",(0,0),(-1,-1),"CENTER"),

    ("BOTTOMPADDING",(0,0),(-1,0),10)

]))

story.append(table)

story.append(Spacer(1,20))

# --------------------------------------------------
# Missing Values
# --------------------------------------------------

story.append(
    Paragraph(
        "<b>3. Missing Value Analysis</b>",
        styles["Heading2"]
    )
)

story.append(
    Paragraph(
        """
        The dataset contained missing values in several numerical and
        categorical columns. Before model development, these missing
        values were carefully analyzed and later handled using
        appropriate preprocessing techniques.
        """,
        styles["BodyText"]
    )
)

story.append(Spacer(1,10))

story.append(
    Image(
        "/static/images/missing_values.png",
        width=420,
        height=220
    )
)

story.append(Spacer(1,10))

story.append(
    Paragraph(
        "<b>Observation:</b> Missing values were mainly concentrated in a few features, indicating the need for data imputation before model training.",
        styles["BodyText"]
    )
)

story.append(Spacer(1,20))

# --------------------------------------------------
# SalePrice Distribution
# --------------------------------------------------

story.append(
    Paragraph(
        "<b>4. Target Variable Distribution</b>",
        styles["Heading2"]
    )
)

story.append(
    Paragraph(
        """
        Understanding the target variable distribution is important
        before building regression models. The SalePrice distribution
        helps identify skewness and the presence of extreme values.
        """,
        styles["BodyText"]
    )
)

story.append(Spacer(1,10))

story.append(
    Image(
        "/static/images/saleprice_distribution.png",
        width=420,
        height=220
    )
)

story.append(Spacer(1,10))

story.append(
    Paragraph(
        "<b>Observation:</b> SalePrice shows a positively skewed distribution, suggesting that transformation techniques such as log transformation may improve model performance.",
        styles["BodyText"]
    )
)

story.append(Spacer(1,20))

# --------------------------------------------------
# Correlation Heatmap
# --------------------------------------------------

story.append(
    Paragraph(
        "<b>5. Correlation Analysis</b>",
        styles["Heading2"]
    )
)

story.append(
    Paragraph(
        """
        Correlation analysis identifies relationships between numerical
        variables and the target variable. Highly correlated features
        generally contribute more to prediction accuracy.
        """,
        styles["BodyText"]
    )
)

story.append(Spacer(1,10))

story.append(
    Image(
        "/static/images/correlation_heatmap.png",
        width=420,
        height=250
    )
)

story.append(Spacer(1,10))

story.append(
    Paragraph(
        "<b>Observation:</b> OverallQual, GrLivArea, GarageCars and TotalBsmtSF show strong positive correlation with SalePrice and are important predictive features.",
        styles["BodyText"]
    )
)

story.append(Spacer(1,20))

# --------------------------------------------------
# Key Findings
# --------------------------------------------------

story.append(
    Paragraph(
        "<b>6. Key Findings</b>",
        styles["Heading2"]
    )
)

findings = """
• The dataset contains both numerical and categorical features.<br/><br/>
• Missing values were identified and prepared for preprocessing.<br/><br/>
• The target variable exhibits positive skewness.<br/><br/>
• Several housing characteristics have a strong influence on sale price.<br/><br/>
• Exploratory analysis provided valuable insights for feature selection and model development.
"""

story.append(
    Paragraph(
        findings,
        styles["BodyText"]
    )
)

story.append(Spacer(1,20))

# --------------------------------------------------
# Conclusion
# --------------------------------------------------

story.append(
    Paragraph(
        "<b>7. Conclusion</b>",
        styles["Heading2"]
    )
)

story.append(
    Paragraph(
        """
        Exploratory Data Analysis provided a comprehensive understanding
        of the dataset by identifying missing values, understanding
        feature distributions and discovering relationships between
        important variables. These insights guided the preprocessing
        stage and contributed to building more accurate regression
        models for house price prediction.
        """,
        styles["BodyText"]
    )
)

doc.build(story)

print("EDA Report Created Successfully.")