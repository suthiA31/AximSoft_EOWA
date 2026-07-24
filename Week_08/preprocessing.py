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

doc = SimpleDocTemplate("/home/aximsoft/Documents/AximSoft_EOWA/Week_08/Notebooks/dataset/reports/preprocessing_report.pdf")

story = []

# -------------------------------------------------------
# TITLE
# -------------------------------------------------------

story.append(
    Paragraph(
        "<b>DATA PREPROCESSING REPORT</b>",
        styles["Title"]
    )
)

story.append(Spacer(1,20))

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

story.append(Spacer(1,20))

# -------------------------------------------------------
# OBJECTIVE
# -------------------------------------------------------

story.append(
    Paragraph(
        "<b>1. Objective</b>",
        styles["Heading2"]
    )
)

story.append(
    Paragraph(
        """
        Data preprocessing is an essential step in machine learning.
        The objective of preprocessing is to improve data quality by
        handling missing values, removing inconsistencies, treating
        outliers, encoding categorical variables and scaling numerical
        features before model development.
        """,
        styles["BodyText"]
    )
)

story.append(Spacer(1,20))

# -------------------------------------------------------
# PREPROCESSING SUMMARY
# -------------------------------------------------------

story.append(
    Paragraph(
        "<b>2. Preprocessing Summary</b>",
        styles["Heading2"]
    )
)

summary = [

    ["Operation","Status"],

    ["Missing Values","Handled"],

    ["Duplicate Records","Removed"],

    ["Outlier Treatment","Completed"],

    ["Categorical Encoding","Completed"],

    ["Feature Scaling","Applied"],

    ["Skewness Reduction","Applied"],

    ["Feature Selection","Completed"]

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

# -------------------------------------------------------
# MISSING VALUES
# -------------------------------------------------------

story.append(
    Paragraph(
        "<b>3. Missing Value Handling</b>",
        styles["Heading2"]
    )
)

story.append(
    Paragraph(
        """
        Missing values were identified during data exploration.
        Numerical features were imputed using the median, while
        categorical features were filled using the most frequent
        value or an appropriate category where necessary.
        """,
        styles["BodyText"]
    )
)

story.append(Spacer(1,10))


story.append(Spacer(1,15))

story.append(
    Paragraph(
        "<b>Observation:</b> After preprocessing, all missing values were successfully handled, ensuring a complete dataset for model training.",
        styles["BodyText"]
    )
)

story.append(Spacer(1,20))

# -------------------------------------------------------
# OUTLIERS
# -------------------------------------------------------

story.append(
    Paragraph(
        "<b>4. Outlier Treatment</b>",
        styles["Heading2"]
    )
)

story.append(
    Paragraph(
        """
        Extreme values were identified using box plots and statistical
        analysis. Appropriate outlier treatment techniques were applied
        to reduce their impact while preserving meaningful observations.
        """,
        styles["BodyText"]
    )
)

# If you have an outlier image, uncomment these lines
# story.append(Image("../reports/images/outlier_boxplot.png",
#                    width=420,
#                    height=220))

story.append(Spacer(1,20))

# -------------------------------------------------------
# ENCODING & SCALING
# -------------------------------------------------------

story.append(
    Paragraph(
        "<b>5. Encoding and Feature Scaling</b>",
        styles["Heading2"]
    )
)

story.append(
    Paragraph(
        """
        Categorical variables were converted into numerical form using
        encoding techniques. Numerical features were standardized using
        StandardScaler to ensure consistent feature scales and improve
        regression model performance.
        """,
        styles["BodyText"]
    )
)

story.append(Spacer(1,20))

# -------------------------------------------------------
# FEATURE ENGINEERING
# -------------------------------------------------------

story.append(
    Paragraph(
        "<b>6. Feature Engineering</b>",
        styles["Heading2"]
    )
)

story.append(
    Paragraph(
        """
        Important features were selected based on correlation analysis
        and domain knowledge. Log transformation was applied to reduce
        skewness in highly skewed numerical features, resulting in a
        more balanced data distribution.
        """,
        styles["BodyText"]
    )
)

story.append(Spacer(1,20))

# -------------------------------------------------------
# KEY IMPROVEMENTS
# -------------------------------------------------------

story.append(
    Paragraph(
        "<b>7. Key Improvements</b>",
        styles["Heading2"]
    )
)

story.append(
    Paragraph(
        """
        • Missing values successfully handled.<br/><br/>
        • Duplicate records removed.<br/><br/>
        • Outliers treated to reduce noise.<br/><br/>
        • Categorical features encoded.<br/><br/>
        • Numerical features scaled.<br/><br/>
        • Skewed features transformed using logarithmic scaling.<br/><br/>
        • Final dataset prepared for regression model development.
        """,
        styles["BodyText"]
    )
)

story.append(Spacer(1,20))

# -------------------------------------------------------
# CONCLUSION
# -------------------------------------------------------

story.append(
    Paragraph(
        "<b>8. Conclusion</b>",
        styles["Heading2"]
    )
)

story.append(
    Paragraph(
        """
        Data preprocessing significantly improved the quality and
        consistency of the dataset. By addressing missing values,
        outliers, encoding, scaling and feature engineering, the
        dataset became suitable for training accurate and reliable
        regression models for house price prediction.
        """,
        styles["BodyText"]
    )
)

doc.build(story)

print("Preprocessing Report Created Successfully.")