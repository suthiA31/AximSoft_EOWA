from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import pandas as pd

# ---------------------------------------
# Feature Importance Data
# ---------------------------------------

importance = pd.DataFrame({

    "Feature":[
        "Overall Quality",
        "Living Area",
        "Basement Area",
        "Year Built",
        "Garage Cars",
        "Full Bathrooms"
    ],

    "Importance":[
        0.513,
        0.213,
        0.138,
        0.081,
        0.046,
        0.008
    ]

})

styles = getSampleStyleSheet()

doc = SimpleDocTemplate(
    "/home/aximsoft/Documents/AximSoft_EOWA/Week_08/Notebooks/dataset/reports/model_interpretation.pdf"
)

story = []

# =======================================================
# TITLE
# =======================================================

story.append(
    Paragraph(
        "<b>MODEL INTERPRETATION REPORT</b>",
        styles["Title"]
    )
)

story.append(Spacer(1,20))

story.append(
    Paragraph(
        "Project : Advanced Regression Model Comparison & Optimization Platform",
        styles["Normal"]
    )
)

story.append(Spacer(1,20))

# =======================================================
# BUSINESS OBJECTIVE
# =======================================================

story.append(
    Paragraph(
        "<b>1. Business Objective</b>",
        styles["Heading2"]
    )
)

story.append(
    Paragraph(
        """
        The objective of this project is to predict residential
        house prices using machine learning regression algorithms.
        Accurate predictions assist buyers, sellers, real estate
        agencies and financial institutions in making better
        pricing decisions.
        """,
        styles["BodyText"]
    )
)

story.append(Spacer(1,20))

# =======================================================
# DATASET OVERVIEW
# =======================================================

story.append(
    Paragraph(
        "<b>2. Dataset Overview</b>",
        styles["Heading2"]
    )
)

dataset = [

    ["Property","Value"],

    ["Dataset","House Prices - Advanced Regression"],

    ["Records","1460"],

    ["Features","80"],

    ["Target Variable","SalePrice"],

    ["Missing Values","Handled"],

    ["Outliers","Treated"],

    ["Encoding","Applied"],

    ["Scaling","Completed"]

]

table = Table(dataset)

table.setStyle(TableStyle([

("BACKGROUND",(0,0),(-1,0),colors.darkblue),

("TEXTCOLOR",(0,0),(-1,0),colors.white),

("GRID",(0,0),(-1,-1),1,colors.black),

("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),

("ALIGN",(0,0),(-1,-1),"CENTER"),

("BOTTOMPADDING",(0,0),(-1,0),10)

]))

story.append(table)

story.append(Spacer(1,25))

# =======================================================
# FEATURE IMPORTANCE
# =======================================================

story.append(
    Paragraph(
        "<b>3. Feature Importance</b>",
        styles["Heading2"]
    )
)

story.append(
    Paragraph(
        """
        Feature importance measures how much each feature contributes
        towards predicting the final house price. Higher importance
        indicates greater influence on the model prediction.
        """,
        styles["BodyText"]
    )
)

story.append(Spacer(1,10))

feature_table = [["Feature","Importance"]]

feature_table += importance.values.tolist()

table = Table(feature_table)

table.setStyle(TableStyle([

("BACKGROUND",(0,0),(-1,0),colors.darkgreen),

("TEXTCOLOR",(0,0),(-1,0),colors.white),

("GRID",(0,0),(-1,-1),1,colors.black),

("BACKGROUND",(0,1),(-1,-1),colors.beige),

("ALIGN",(0,0),(-1,-1),"CENTER")

]))

story.append(table)

story.append(Spacer(1,20))

# =======================================================
# FEATURE EXPLANATION
# =======================================================

story.append(
    Paragraph(
        "<b>4. Feature Interpretation</b>",
        styles["Heading2"]
    )
)

explanations = [

("Overall Quality",
"Overall quality has the greatest impact on selling price. Better construction quality generally leads to significantly higher property values."),

("Living Area",
"Larger living areas provide more usable space and therefore increase the market value of the property."),

("Basement Area",
"Houses with larger finished basements generally attract higher selling prices."),

("Year Built",
"Newer houses often require less maintenance and include modern amenities, making them more valuable."),

("Garage Cars",
"A larger garage improves convenience and contributes positively to property value."),

("Full Bathrooms",
"Additional bathrooms improve functionality and slightly increase selling price.")

]

for title, desc in explanations:

    story.append(
        Paragraph(
            f"<b>{title}</b>",
            styles["Heading3"]
        )
    )

    story.append(
        Paragraph(
            desc,
            styles["BodyText"]
        )
    )

story.append(Spacer(1,20))

# =======================================================
# BUSINESS INSIGHTS
# =======================================================

story.append(
    Paragraph(
        "<b>5. Business Insights</b>",
        styles["Heading2"]
    )
)

insights = [

"• Houses with higher construction quality consistently achieve higher selling prices.",

"• Increasing living area significantly improves property value.",

"• Recently constructed houses generally outperform older properties in market price.",

"• Basement space adds additional market value.",

"• Garage capacity positively influences buyer decisions.",

"• Proper preprocessing improved prediction accuracy across all regression models."

]

for item in insights:

    story.append(
        Paragraph(
            item,
            styles["BodyText"]
        )
    )

story.append(Spacer(1,20))

# =======================================================
# MODEL INTERPRETATION
# =======================================================

story.append(
    Paragraph(
        "<b>6. Prediction Interpretation</b>",
        styles["Heading2"]
    )
)

story.append(
    Paragraph(
        """
        The deployed Random Forest Regressor evaluates multiple
        property characteristics simultaneously before estimating
        the final selling price. Instead of relying on a single
        factor, the model combines information from all important
        housing features to generate a reliable prediction.
        """,
        styles["BodyText"]
    )
)

story.append(Spacer(1,20))

# =======================================================
# BUSINESS RECOMMENDATIONS
# =======================================================

story.append(
    Paragraph(
        "<b>7. Business Recommendations</b>",
        styles["Heading2"]
    )
)

recommendations = [

"• Improve overall construction quality before selling a property.",

"• Renovating living spaces can substantially increase resale value.",

"• Additional garage capacity improves buyer interest.",

"• Modernizing older homes increases market competitiveness.",

"• Use the prediction system as a decision-support tool rather than replacing professional property valuation."

]

for item in recommendations:

    story.append(
        Paragraph(
            item,
            styles["BodyText"]
        )
    )

story.append(Spacer(1,20))

# =======================================================
# ADVANTAGES
# =======================================================

story.append(
    Paragraph(
        "<b>8. Advantages of the Selected Model</b>",
        styles["Heading2"]
    )
)

story.append(
    Paragraph(
        """
        • High prediction accuracy.<br/>
        • Handles nonlinear relationships effectively.<br/>
        • Robust against overfitting.<br/>
        • Suitable for real-world property valuation applications.<br/>
        • Performs consistently across different housing characteristics.
        """,
        styles["BodyText"]
    )
)

story.append(Spacer(1,20))

# =======================================================
# CONCLUSION
# =======================================================

story.append(
    Paragraph(
        "<b>9. Conclusion</b>",
        styles["Heading2"]
    )
)

story.append(
    Paragraph(
        """
        Based on the experimental evaluation and feature analysis,
        the Random Forest Regressor was selected as the final model
        for deployment. The model demonstrated reliable prediction
        performance and identified Overall Quality and Living Area
        as the most influential factors affecting residential house
        prices. The developed system can assist buyers, sellers,
        real estate professionals and financial institutions in
        making informed pricing decisions.
        """,
        styles["BodyText"]
    )
)

doc.build(story)

print("Model Interpretation Report Created Successfully.")