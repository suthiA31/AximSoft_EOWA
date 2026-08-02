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

import os

REPORT_FOLDER = "reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)


def create_diagnosis_report(
        uploaded_image,
        gradcam_image,
        prediction,
        confidence,
        probabilities,
        disease_details
):

    pdf_path = os.path.join(
        REPORT_FOLDER,
        "Diagnosis_Report.pdf"
    )

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    story = []

    # ---------------------------------------

    title = Paragraph(
        "<b>Skin Disease Diagnosis Report</b>",
        styles["Title"]
    )

    story.append(title)

    story.append(Spacer(1,20))

    # ---------------------------------------

    story.append(
        Paragraph(
            "<b>Prediction Result</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"Disease : <b>{prediction}</b>",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Confidence : <b>{confidence:.2f}%</b>",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1,20))

    # ---------------------------------------

    story.append(
        Paragraph(
            "<b>Probability Scores</b>",
            styles["Heading2"]
        )
    )

    table_data = [["Disease","Probability (%)"]]

    for disease, prob in probabilities.items():

        table_data.append(
            [disease, str(prob)]
        )

    table = Table(table_data)

    table.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(-1,0),colors.pink),

        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("GRID",(0,0),(-1,-1),1,colors.grey),

        ("BACKGROUND",(0,1),(-1,-1),colors.beige),

        ("ALIGN",(0,0),(-1,-1),"CENTER")

    ]))

    story.append(table)

    story.append(Spacer(1,20))

    # ---------------------------------------

    story.append(
        Paragraph(
            "<b>Disease Information</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            disease_details["description"],
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Risk :</b> {disease_details['risk']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Recommendation :</b> {disease_details['recommendation']}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1,20))

    # ---------------------------------------

    if os.path.exists(uploaded_image):

        story.append(
            Paragraph(
                "<b>Uploaded Image</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Image(
                uploaded_image,
                width=200,
                height=200
            )
        )

        story.append(Spacer(1,20))

    # ---------------------------------------

    if os.path.exists(gradcam_image):

        story.append(
            Paragraph(
                "<b>Grad-CAM Visualization</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Image(
                gradcam_image,
                width=200,
                height=200
            )
        )

    # ---------------------------------------

    story.append(Spacer(1,30))

    story.append(

        Paragraph(

        "<font color='red'><b>Medical Disclaimer</b></font><br/>"

        "This prediction is generated using a deep learning model "

        "for educational purposes only. Please consult a qualified "

        "dermatologist for medical diagnosis.",

        styles["BodyText"]

        )

    )

    doc.build(story)

    return pdf_path