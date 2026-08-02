from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.colors import HexColor

import os

os.makedirs("reports", exist_ok=True)

styles = getSampleStyleSheet()

title = styles["Heading1"]
title.alignment = TA_CENTER

heading = styles["Heading2"]
normal = styles["BodyText"]


def create_evaluation_report():

    doc = SimpleDocTemplate(
        "static/reports/Model_Evaluation_Report.pdf"
    )

    elements = []

    elements.append(
        Paragraph(
            "Skin Disease Classification<br/>Model Evaluation Report",
            title
        )
    )

    elements.append(Spacer(1,20))

    elements.append(
        Paragraph("Evaluation Metrics",heading)
    )

    elements.append(Spacer(1,10))

    metrics = [

        ["Metric","Value"],

        ["Accuracy","72.39%"],

        ["Precision","68.35%"],

        ["Recall","72.39%"],

        ["F1 Score","68.21%"],

        ["ROC-AUC","83.49%"]

    ]

    table = Table(metrics,colWidths=[200,150])

    table.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(-1,0),HexColor("#ff5c8a")),

        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("GRID",(0,0),(-1,-1),1,colors.grey),

        ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),

        ("ALIGN",(0,0),(-1,-1),"CENTER")

    ]))

    elements.append(table)

    elements.append(Spacer(1,20))

    elements.append(
        Paragraph(
            "Performance Summary",
            heading
        )
    )

    elements.append(
        Paragraph(
            """
            The final EfficientNetB0 model demonstrated strong
            classification performance on the HAM10000 skin lesion
            dataset. The model achieved 72.39% accuracy while
            maintaining balanced precision, recall and F1-score.
            ROC-AUC score of 83.49% indicates good discrimination
            between disease classes.
            """,
            normal
        )
    )

    elements.append(Spacer(1,20))

    elements.append(
        Paragraph(
            "Evaluation Techniques",
            heading
        )
    )

    bullets = [
        "Train / Validation / Test Split",
        "Classification Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC-AUC",
        "Confusion Matrix",
        "Grad-CAM Explainability"
    ]

    for item in bullets:

        elements.append(
            Paragraph("• "+item,normal)
        )

    doc.build(elements)


if __name__ == "__main__":

    create_evaluation_report()