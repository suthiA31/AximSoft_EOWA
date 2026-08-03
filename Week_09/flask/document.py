from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

# ============================================================
# Create Document
# ============================================================

document = Document()

# ============================================================
# Title
# ============================================================

title = document.add_heading(
    "Advanced Deep Learning Project",
    level=0
)
title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

subtitle = document.add_heading(
    "Multi-Class Skin Disease Classification & Diagnosis Platform",
    level=1
)
subtitle.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

document.add_paragraph()

document.add_heading("Project Information", level=1)

table = document.add_table(rows=6, cols=2)
table.style = "Table Grid"

info = [
    ("Project", "Skin Disease Diagnosis Platform"),
    ("Dataset", "HAM10000"),
    ("Technology", "TensorFlow, Keras, Flask"),
    ("Programming Language", "Python"),
    ("Frontend", "HTML, CSS, Bootstrap"),
    ("Report", "Final Project Documentation")
]

for row, value in zip(table.rows, info):
    row.cells[0].text = value[0]
    row.cells[1].text = value[1]

document.add_page_break()

# ============================================================
# Project Overview
# ============================================================

document.add_heading("1. Project Overview", level=1)

document.add_paragraph(
"""
Skin diseases are among the most common health problems worldwide.
Manual diagnosis requires experienced dermatologists and may consume
considerable time. Deep learning techniques provide an automated
approach for detecting skin diseases from dermoscopic images.

The objective of this project is to develop a web-based skin disease
diagnosis platform capable of accurately classifying seven categories
of skin diseases using Convolutional Neural Networks and Transfer
Learning models.
"""
)

document.add_heading("Objectives", level=2)

objectives = [
"Develop an automated skin disease classifier.",
"Train multiple CNN and Transfer Learning models.",
"Deploy the best model using Flask.",
"Generate Grad-CAM heatmaps.",
"Generate PDF diagnosis reports.",
"Provide analytics dashboards."
]

for item in objectives:
    document.add_paragraph(item, style="List Bullet")

document.add_heading("Project Workflow", level=2)

document.add_paragraph(
"""
Dataset Collection

↓

Preprocessing

↓

Data Augmentation

↓

Model Training

↓

Evaluation

↓

Prediction

↓

Grad-CAM

↓

Flask Deployment
"""
)

document.add_paragraph(
"[Insert Workflow Screenshot Here]"
)

document.add_page_break()

# ============================================================
# Dataset
# ============================================================

document.add_heading("2. Dataset and Data Preprocessing", level=1)

document.add_paragraph(
"""
The HAM10000 dataset contains dermoscopic images belonging to seven
different skin disease classes. Images were resized to 128×128 pixels,
normalized, augmented and divided into training, validation and
testing subsets.
"""
)

table = document.add_table(rows=6, cols=2)
table.style = "Table Grid"

rows = [
("Dataset","HAM10000"),
("Images","10015"),
("Classes","7"),
("Image Size","128 x 128"),
("Train Split","70%"),
("Validation/Test","15% / 15%")
]

for r,data in zip(table.rows,rows):
    r.cells[0].text=data[0]
    r.cells[1].text=data[1]

document.add_heading("Preprocessing Steps", level=2)

steps = [
"Loaded metadata and image files.",
"Mapped image paths.",
"Removed inconsistencies.",
"Encoded disease labels.",
"Resized images.",
"Normalized pixel values.",
"Applied data augmentation.",
"Computed class weights.",
"Created training, validation and testing datasets."
]

for s in steps:
    document.add_paragraph(s, style="List Bullet")

document.add_paragraph(
"[Insert Dataset Distribution Chart Here]"
)

document.add_paragraph(
"[Insert Sample Images Here]"
)

document.add_page_break()

# ============================================================
# Model Training
# ============================================================

document.add_heading("3. Model Training", level=1)

document.add_paragraph(
"""
Several deep learning architectures were developed and evaluated.
Transfer learning techniques significantly improved performance over
baseline CNN models.
"""
)

table=document.add_table(rows=8,cols=6)
table.style="Table Grid"

headers=[
"Model",
"Accuracy",
"Precision",
"Recall",
"F1",
"ROC"
]

for i,h in enumerate(headers):
    table.rows[0].cells[i].text=h

models=[
["Basic CNN","67.27","68.37","67.27","65.51","86.14"],
["BatchNorm","61.68","76.94","61.68","66.02","90.32"],
["Deep CNN","67.53","49.61","59.08","67.53","80.60"],
["MobileNetV2","59.08","72.50","59.08","62.96","85.33"],
["ResNet50","66.93","44.80","66.93","53.67","51.02"],
["DenseNet121","20.09","61.09","20.09","28.44","59.98"],
["EfficientNetB0","72.39","68.35","72.39","68.21","83.49"]
]

for i,row in enumerate(models):
    for j,val in enumerate(row):
        table.rows[i+1].cells[j].text=val

document.add_heading("Best Performing Model", level=2)

document.add_paragraph(
"""
EfficientNetB0 achieved the highest overall accuracy among all models.
It demonstrated superior generalization and stable convergence after
fine-tuning with class weights and early stopping.
"""
)

document.add_paragraph(
"[Insert Accuracy Graph Here]"
)

document.add_page_break()

# ============================================================
# Flask
# ============================================================

document.add_heading("4. Flask Web Application", level=1)

document.add_paragraph(
"""
A Flask web application was developed to provide an interactive
interface for end users.

The application consists of the following modules.
"""
)

pages=[
"Home",
"Dashboard",
"Analytics",
"Prediction",
"Grad-CAM",
"Reports",
"About"
]

for p in pages:
    document.add_paragraph(p,style="List Bullet")

document.add_paragraph(
"[Insert Home Screenshot]"
)

document.add_paragraph(
"[Insert Dashboard Screenshot]"
)

document.add_paragraph(
"[Insert Prediction Screenshot]"
)

document.add_page_break()

# ============================================================
# Explainable AI
# ============================================================

document.add_heading("5. Explainable AI", level=1)

document.add_paragraph(
"""
Grad-CAM was integrated into the application to visualize the
important regions that influenced the model's prediction.

This improves transparency and assists users in understanding how the
deep learning model reached its decision.
"""
)

document.add_paragraph(
"[Insert Original Image]"
)

document.add_paragraph(
"[Insert Grad-CAM Heatmap]"
)

document.add_page_break()

# ============================================================
# Conclusion
# ============================================================

document.add_heading("6. Conclusion", level=1)

document.add_paragraph(
"""
An end-to-end deep learning platform for skin disease diagnosis was
successfully developed. Multiple CNN and Transfer Learning models were
trained and evaluated. EfficientNetB0 achieved the highest
classification performance and was deployed through a Flask web
application. The system also includes Grad-CAM visualization,
interactive dashboards, analytics pages and automated report
generation.
"""
)

document.add_heading("Future Enhancements", level=2)

future=[
"Increase dataset size.",
"Deploy on cloud.",
"Develop mobile application.",
"Improve accuracy using ensemble learning.",
"Integrate hospital databases.",
"Support real-time diagnosis."
]

for f in future:
    document.add_paragraph(f,style="List Bullet")

# ============================================================
# Save
# ============================================================

document.save("Skin_Disease_Project_Report.docx")

print("Report Created Successfully.")