from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.colors import HexColor
from reportlab.platypus.tables import Table, TableStyle

import os

os.makedirs("reports", exist_ok=True)

styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = TA_CENTER

heading = styles["Heading2"]
normal = styles["BodyText"]


def create_model_report():

    doc = SimpleDocTemplate(
        "static/reports/Model_Comparison_Report.pdf"
    )

    elements = []

    elements.append(Paragraph(
        "Skin Disease Classification<br/>Model Comparison Report",
        title_style
    ))

    elements.append(Spacer(1,20))

    data = [

        ["Model","Accuracy","Precision","Recall","F1","ROC-AUC"],

        ["Basic CNN","67.27%","68.37%","67.27%","65.51%","86.13%"],

        ["Batch Normalization","61.67%","76.94%","61.67%","66.02%","90.31%"],

        ["Deep CNN","67.53%","49.61%","59.08%","67.53%","80.59%"],

        ["MobileNetV2","59.08%","72.50%","59.08%","62.96%","85.33%"],

        ["ResNet50","66.93%","44.80%","66.93%","53.67%","51.02%"],

        ["DenseNet121","20.09%","61.09%","20.09%","28.44%","59.98%"],

        ["EfficientNetB0","72.39%","68.35%","72.39%","68.21%","83.49%"]

    ]

    table = Table(data)

    table.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(-1,0),HexColor("#ff5c8a")),

        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("GRID",(0,0),(-1,-1),1,colors.grey),

        ("ALIGN",(0,0),(-1,-1),"CENTER"),

        ("BACKGROUND",(0,1),(-1,-1),colors.beige),

        ("BOTTOMPADDING",(0,0),(-1,0),12)

    ]))

    elements.append(table)

    elements.append(Spacer(1,30))

    elements.append(Paragraph(
        "<b>Best Model :</b> EfficientNetB0 achieved the highest "
        "classification accuracy of <b>72.39%</b> among all evaluated models.",
        normal
    ))

    doc.build(elements)


if __name__ == "__main__":

    create_model_report()