import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import inch

# ======================================================
# Create Reports Folder
# ======================================================

os.makedirs("reports", exist_ok=True)

pdf = SimpleDocTemplate(
    "static/reports/Explainable_AI_Report.pdf"
)

styles = getSampleStyleSheet()

title = styles["Heading1"]
title.alignment = TA_CENTER
title.textColor = colors.HexColor("#d63384")

heading = styles["Heading2"]
heading.textColor = colors.HexColor("#d63384")

normal = styles["BodyText"]

story = []

# ======================================================
# TITLE
# ======================================================

story.append(Paragraph(
    "EXPLAINABLE AI REPORT",
    title
))

story.append(Spacer(1,0.3*inch))

story.append(Paragraph(
    "<b>Project:</b> Multi-Class Skin Disease Classification & Diagnosis Platform",
    normal
))

story.append(Paragraph(
    "<b>Explainability Method:</b> Grad-CAM (Gradient-weighted Class Activation Mapping)",
    normal
))

story.append(Spacer(1,0.3*inch))

# ======================================================
# INTRODUCTION
# ======================================================

story.append(Paragraph(
    "1. Introduction",
    heading
))

story.append(Paragraph(
"""
Artificial Intelligence models often behave like black boxes, making it
difficult to understand why a particular prediction was made.
Explainable Artificial Intelligence (XAI) addresses this issue by
providing visual explanations that help users understand the decision-
making process of deep learning models.

In this project, Grad-CAM (Gradient-weighted Class Activation Mapping)
was used to visualize the important regions of skin lesion images that
influenced the model during prediction. This improves transparency and
builds confidence in the model's predictions.
""",
normal))

story.append(Spacer(1,0.25*inch))

# ======================================================
# WHY XAI
# ======================================================

story.append(Paragraph(
    "2. Importance of Explainable AI",
    heading
))

story.append(Paragraph(
"""
Medical diagnosis requires reliable and interpretable predictions.
Although deep learning models can achieve high classification accuracy,
their internal decision-making process is often difficult to interpret.

Explainable AI provides visual evidence supporting model predictions.
This allows clinicians, researchers, and users to understand which image
regions contributed most to the classification result, improving trust
and supporting better clinical decision-making.
""",
normal))

story.append(Spacer(1,0.25*inch))

# ======================================================
# HOW GRADCAM WORKS
# ======================================================

story.append(Paragraph(
    "3. Grad-CAM Workflow",
    heading
))

story.append(Paragraph(
"""
Grad-CAM generates a heatmap by computing the gradients of the predicted
class with respect to the feature maps of the last convolutional layer.
The resulting heatmap highlights image regions that have the greatest
influence on the final prediction.

Workflow:

Input Image

↓

Image Preprocessing

↓

Deep Learning Model

↓

Last Convolution Layer

↓

Gradient Calculation

↓

Heatmap Generation

↓

Overlay on Original Image

↓

Visual Explanation
""",
normal))

story.append(Spacer(1,0.25*inch))

# ======================================================
# BENEFITS
# ======================================================

story.append(Paragraph(
    "4. Benefits of Grad-CAM",
    heading
))

benefits = Table([
["Benefit","Description"],
["Visual Interpretation","Highlights important lesion regions"],
["Transparency","Shows why the prediction was made"],
["Model Validation","Verifies that the model focuses on lesion areas"],
["Clinical Support","Helps healthcare professionals interpret predictions"],
["Error Analysis","Assists in identifying incorrect model attention"],
["Trust","Improves confidence in AI-assisted diagnosis"]
])

benefits.setStyle(TableStyle([
("BACKGROUND",(0,0),(-1,0),colors.pink),
("TEXTCOLOR",(0,0),(-1,0),colors.white),
("GRID",(0,0),(-1,-1),1,colors.grey),
("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),
("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")
]))

story.append(benefits)

story.append(Spacer(1,0.3*inch))

# ======================================================
# PROJECT IMPLEMENTATION
# ======================================================

story.append(Paragraph(
    "5. Implementation in This Project",
    heading
))

story.append(Paragraph(
"""
After a user uploads a dermoscopic skin image through the Flask web
application, the trained ResNet50 model predicts one of the seven skin
disease classes. Once the prediction is completed, Grad-CAM extracts the
feature maps from the last convolutional layer of the network.

The gradients of the predicted class are calculated and combined to
produce a class activation heatmap. This heatmap is resized and overlaid
on the original skin lesion image using OpenCV. The final visualization
clearly indicates which regions of the lesion contributed most to the
prediction, enabling users to visually interpret the model's reasoning.
""",
normal))

story.append(Spacer(1,0.25*inch))

# ======================================================
# OUTPUT
# ======================================================

story.append(Paragraph(
    "6. Generated Outputs",
    heading
))

output = Table([
["Output","Purpose"],
["Predicted Disease","Displays the predicted skin disease"],
["Confidence Score","Shows prediction confidence"],
["Probability Distribution","Displays probabilities for all classes"],
["Grad-CAM Heatmap","Highlights influential image regions"],
["Disease Information","Provides description and recommendations"]
])

output.setStyle(TableStyle([
("BACKGROUND",(0,0),(-1,0),colors.lightpink),
("GRID",(0,0),(-1,-1),1,colors.grey),
("BACKGROUND",(0,1),(-1,-1),colors.beige),
("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")
]))

story.append(output)

story.append(Spacer(1,0.3*inch))

# ======================================================
# CONCLUSION
# ======================================================

story.append(Paragraph(
    "7. Conclusion",
    heading
))

story.append(Paragraph(
"""
Explainable AI enhances the transparency and reliability of deep
learning models by providing meaningful visual explanations for their
predictions. The integration of Grad-CAM into this skin disease
diagnosis platform enables users to understand which regions of the skin
lesion influenced the model's decision. This not only increases trust in
the AI system but also supports healthcare professionals by offering an
additional layer of visual interpretation. The Explainable AI component
makes the developed application more informative, interpretable, and
suitable for educational and research purposes.
""",
normal))

pdf.build(story)

print("Explainable AI Report Generated Successfully!")