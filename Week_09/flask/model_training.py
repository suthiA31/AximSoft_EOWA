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
    "static/reports/Model_Training_Report.pdf"
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
    "MODEL TRAINING REPORT",
    title
))

story.append(Spacer(1,0.3*inch))

story.append(Paragraph(
    "<b>Project:</b> Multi-Class Skin Disease Classification & Diagnosis Platform",
    normal
))

story.append(Paragraph(
    "<b>Dataset:</b> HAM10000",
    normal
))

story.append(Paragraph(
    "<b>Framework:</b> TensorFlow / Keras",
    normal
))

story.append(Spacer(1,0.3*inch))

# ======================================================
# INTRODUCTION
# ======================================================

story.append(Paragraph(
    "1. Training Overview",
    heading
))

story.append(Paragraph(
"""
The objective of model training was to develop an accurate deep learning
model capable of classifying dermoscopic skin lesion images into seven
disease categories. Multiple convolutional neural network (CNN) models
and transfer learning architectures were trained and evaluated to
identify the best-performing model.

The training process involved image preprocessing, data augmentation,
class balancing using class weights, optimization using different
learning strategies, and model evaluation using several performance
metrics.
""",
normal))

story.append(Spacer(1,0.25*inch))

# ======================================================
# MODELS
# ======================================================

story.append(Paragraph(
    "2. Models Trained",
    heading
))

table = Table([

["Model","Description"],

["Basic CNN","Baseline convolutional neural network"],

["CNN + Batch Normalization","Improved training stability"],

["Deep CNN","Additional convolution layers"],

["MobileNetV2","Transfer Learning"],

["ResNet50","Transfer Learning"],

["DenseNet121","Transfer Learning"],

["EfficientNetB0","Transfer Learning + Fine Tuning"]

])

table.setStyle(TableStyle([

("BACKGROUND",(0,0),(-1,0),colors.pink),

("TEXTCOLOR",(0,0),(-1,0),colors.white),

("GRID",(0,0),(-1,-1),1,colors.grey),

("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),

("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")

]))

story.append(table)

story.append(Spacer(1,0.3*inch))

# ======================================================
# TRAINING CONFIGURATION
# ======================================================

story.append(Paragraph(
    "3. Training Configuration",
    heading
))

story.append(Paragraph(
"""
The models were trained using TensorFlow and Keras. Images were resized
to 128 × 128 pixels before being supplied to the neural networks.
Categorical cross-entropy was used as the loss function because the
problem involves multi-class classification.

Different optimizers including Adam and RMSprop were evaluated during
training. Early Stopping was employed to monitor validation loss and
prevent unnecessary epochs, while learning rate scheduling was used to
improve convergence. Class weights were applied to compensate for the
imbalanced distribution of disease categories within the HAM10000
dataset.
""",
normal))

story.append(Spacer(1,0.25*inch))

# ======================================================
# HYPERPARAMETERS
# ======================================================

story.append(Paragraph(
    "4. Hyperparameter Settings",
    heading
))

table = Table([

["Parameter","Value"],

["Image Size","128 × 128"],

["Batch Size","32"],

["Optimizer","Adam / RMSprop"],

["Loss Function","Categorical Crossentropy"],

["Epochs","50"],

["Callbacks","EarlyStopping"],

["Learning Rate","0.001"],

["Class Weights","Enabled"]

])

table.setStyle(TableStyle([

("BACKGROUND",(0,0),(-1,0),colors.lightpink),

("GRID",(0,0),(-1,-1),1,colors.grey),

("BACKGROUND",(0,1),(-1,-1),colors.beige),

("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")

]))

story.append(table)

story.append(Spacer(1,0.25*inch))

# ======================================================
# TRANSFER LEARNING
# ======================================================

story.append(Paragraph(
    "5. Transfer Learning",
    heading
))

story.append(Paragraph(
"""
Transfer learning was employed using pretrained convolutional neural
networks initialized with ImageNet weights. Initially, the pretrained
feature extractor layers were frozen while the custom classification
head was trained. During fine-tuning, selected upper layers of the
pretrained network were unfrozen, allowing the model to learn
domain-specific skin lesion features while retaining useful visual
representations learned from large-scale datasets.

Among all transfer learning models, EfficientNetB0 achieved the best
overall classification performance.
""",
normal))

story.append(Spacer(1,0.25*inch))

# ======================================================
# PERFORMANCE
# ======================================================

story.append(Paragraph(
    "6. Final Model Performance",
    heading
))

table = Table([

["Metric","Value"],

["Accuracy","72.39 %"],

["Precision","68.35 %"],

["Recall","72.39 %"],

["F1 Score","68.21 %"],

["ROC-AUC","83.49 %"]

])

table.setStyle(TableStyle([

("BACKGROUND",(0,0),(-1,0),colors.pink),

("TEXTCOLOR",(0,0),(-1,0),colors.white),

("GRID",(0,0),(-1,-1),1,colors.grey),

("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),

("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")

]))

story.append(table)

story.append(Spacer(1,0.25*inch))

# ======================================================
# CONCLUSION
# ======================================================

story.append(Paragraph(
    "7. Conclusion",
    heading
))

story.append(Paragraph(
"""
The model training process successfully produced several deep learning
models for skin disease classification. Extensive experimentation with
different CNN architectures, transfer learning models, hyperparameter
settings, and optimization strategies resulted in significant
performance improvements. Fine-tuned EfficientNetB0 achieved the highest
classification accuracy among all evaluated models. The trained model
was subsequently integrated into the Flask web application to provide
real-time skin disease prediction, confidence estimation, probability
distribution, and Grad-CAM visual explanations.
""",
normal))

pdf.build(story)

print("Model Training Report Generated Successfully!")