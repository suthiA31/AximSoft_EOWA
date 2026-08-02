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

# ==========================================================
# Create Reports Folder
# ==========================================================

os.makedirs("reports", exist_ok=True)

# ==========================================================
# PDF
# ==========================================================

pdf = SimpleDocTemplate(
    "static/reports/Data_Preprocessing_Report1.pdf"
)

styles = getSampleStyleSheet()

title = styles["Heading1"]
title.alignment = TA_CENTER
title.textColor = colors.HexColor("#d63384")

heading = styles["Heading2"]
heading.textColor = colors.HexColor("#d63384")

normal = styles["BodyText"]

story = []

# ==========================================================
# TITLE
# ==========================================================

story.append(Paragraph(
    "DATA PREPROCESSING REPORT",
    title
))

story.append(Spacer(1, 0.3 * inch))

story.append(Paragraph(
    "<b>Project :</b> Multi-Class Skin Disease Classification and Diagnosis Platform",
    normal
))

story.append(Paragraph(
    "<b>Dataset :</b> HAM10000 Skin Lesion Dataset",
    normal
))

story.append(Paragraph(
    "<b>Total Images :</b> 10,015",
    normal
))

story.append(Spacer(1, 0.3 * inch))

# ==========================================================
# DATASET OVERVIEW
# ==========================================================

story.append(Paragraph(
    "1. Dataset Overview",
    heading
))

story.append(Paragraph(
"""
The HAM10000 dataset is a publicly available dermoscopic image dataset
containing 10,015 skin lesion images collected from different patients.
The dataset consists of seven different skin disease categories including
both benign and malignant lesions. The images are captured using
dermatoscopy, providing high-quality visual information suitable for
deep learning-based medical image classification.

The dataset contains images with varying lesion sizes, colors, shapes,
and textures. Before model training, preprocessing is essential to
standardize the images, improve quality, and prepare them for deep
learning architectures.
""",
normal))

story.append(Spacer(1, 0.25 * inch))

# ==========================================================
# DATASET TABLE
# ==========================================================

story.append(Paragraph(
    "Dataset Summary",
    heading
))

table = Table([

["Property","Value"],

["Dataset","HAM10000"],

["Total Images","10015"],

["Disease Classes","7"],

["Image Format","JPG"],

["Image Size","128 × 128"],

["Color Mode","RGB"],

["Training Images","7009"],

["Validation Images","1503"],

["Testing Images","1503"]

])

table.setStyle(TableStyle([

("BACKGROUND",(0,0),(-1,0),colors.pink),

("TEXTCOLOR",(0,0),(-1,0),colors.white),

("GRID",(0,0),(-1,-1),1,colors.grey),

("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),

("BOTTOMPADDING",(0,0),(-1,0),10),

("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")

]))

story.append(table)

story.append(Spacer(1,0.3*inch))

# ==========================================================
# PREPROCESSING STEPS
# ==========================================================

story.append(Paragraph(
"2. Data Preprocessing Steps",
heading
))

story.append(Paragraph(
"""
The preprocessing pipeline ensures that every image has a consistent
format before entering the neural network. The following preprocessing
operations were performed:

<br/><br/>

• Loaded metadata from HAM10000_metadata.csv.

<br/><br/>

• Mapped image paths from both image folders.

<br/><br/>

• Converted disease labels into numerical labels.

<br/><br/>

• Loaded RGB images using TensorFlow.

<br/><br/>

• Resized every image to 128 × 128 pixels.

<br/><br/>

• Converted images into floating-point tensors.

<br/><br/>

• Normalized pixel values by dividing each pixel by 255.

<br/><br/>

• Created batches using ImageDataGenerator.

<br/><br/>

• Generated train, validation and testing datasets.

<br/><br/>

• Verified dataset integrity before training.

""",
normal))

story.append(Spacer(1,0.25*inch))

# ==========================================================
# AUGMENTATION
# ==========================================================

story.append(Paragraph(
"3. Data Augmentation",
heading
))

story.append(Paragraph(
"""
To improve model generalization and reduce overfitting, multiple image
augmentation techniques were applied during training. These augmentations
generate different variations of existing images while preserving disease
characteristics.

The augmentation techniques include horizontal flipping, vertical
flipping, random rotation, zooming, brightness adjustment, and random
cropping. These operations enable the model to become more robust to
variations in illumination, orientation, and lesion positioning.
""",
normal))

story.append(Spacer(1,0.2*inch))

aug_table = Table([

["Technique","Purpose"],

["Horizontal Flip","Improve Generalization"],

["Vertical Flip","Increase Robustness"],

["Rotation","Handle Orientation Changes"],

["Zoom","Scale Variations"],

["Brightness","Lighting Robustness"]

])

aug_table.setStyle(TableStyle([

("BACKGROUND",(0,0),(-1,0),colors.lightpink),

("GRID",(0,0),(-1,-1),1,colors.grey),

("BACKGROUND",(0,1),(-1,-1),colors.beige),

("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")

]))

story.append(aug_table)

story.append(Spacer(1,0.3*inch))

# ==========================================================
# CLASS WEIGHTS
# ==========================================================

story.append(Paragraph(
"4. Handling Class Imbalance",
heading
))

story.append(Paragraph(
"""
The HAM10000 dataset contains an imbalanced distribution of disease
classes. Certain diseases such as Melanocytic Nevus contain thousands
of images, whereas Dermatofibroma and Vascular Lesion contain relatively
few samples.

To overcome this issue, class weights were computed using the
compute_class_weight() function from Scikit-learn. During model training,
larger weights were assigned to minority classes so that the neural
network paid more attention to underrepresented diseases. This helps
improve fairness and overall classification performance.
""",
normal))

story.append(Spacer(1,0.25*inch))

# ==========================================================
# PIPELINE
# ==========================================================

story.append(Paragraph(
"5. Complete Preprocessing Pipeline",
heading
))

story.append(Paragraph(
"""
HAM10000 Dataset

↓

Metadata Loading

↓

Image Path Mapping

↓

Label Encoding

↓

Resize Images (128 × 128)

↓

Pixel Normalization

↓

Data Augmentation

↓

Train / Validation / Test Split

↓

Class Weight Calculation

↓

Ready for Deep Learning Models
""",
normal))

story.append(Spacer(1,0.25*inch))

# ==========================================================
# CONCLUSION
# ==========================================================

story.append(Paragraph(
"6. Conclusion",
heading
))

story.append(Paragraph(
"""
The preprocessing stage plays an essential role in achieving reliable
skin disease classification performance. Image resizing, normalization,
augmentation, and class balancing improve the quality of the training
data and enable the deep learning models to learn more discriminative
features. The final processed dataset provides a standardized and robust
input for CNN and transfer learning models, contributing to improved
classification accuracy and better generalization on unseen skin lesion
images.
""",
normal))

# ==========================================================
# BUILD PDF
# ==========================================================

pdf.build(story)

print("Data Preprocessing Report Created Successfully!")