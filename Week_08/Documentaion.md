# 🏠 House Price Prediction using Machine Learning

## 📖 Project Overview

This project aims to predict house sale prices using Machine Learning techniques. The project follows a complete Machine Learning workflow, including data cleaning, exploratory data analysis, feature engineering, model training, evaluation, and deployment using Flask.

---

# 📊 Dataset Information

Dataset: House Prices Dataset

Target Variable:
- SalePrice

Total Records:
- Rows : 1460
-Columns : 81

After Cleaning Total Features:
- 76,1460

Numerical Features:
- 38

Categorical Features:
- 43
# Home Page

![Home Page](ss_image/s1.png)
---

# Phase 1&2: Data Cleaning& Understanding

The following preprocessing steps were performed to improve data quality.

### Missing Value Analysis

- Total columns with missing values: 19

Missing value handling methods used:

| Method | Columns |
|---------|----------|
| Median Imputation | LotFrontage |
| Mode Imputation | Electrical, KitchenQual |
| Fill with "None" | Alley, Fence, FireplaceQu |
| Fill with 0 | GarageCars, GarageArea |

### Duplicate Records

- Duplicate rows found: 0
- Duplicate rows removed: 0

### Data Type Corrections

- Converted required columns into appropriate data types.

---

# Phase 2: Exploratory Data Analysis (EDA)

Several visualizations were created to understand the dataset.

Performed Analysis:

- Missing Value Heatmap
- Feature Distribution
- Correlation Matrix
- SalePrice Distribution
- Boxplots for Outlier Detection
- Pairwise Relationship Analysis
- Numerical Feature Summary
- Categorical Feature Frequency

Important Findings

- SalePrice showed right-skewed distribution.
- OverallQual has the highest positive correlation with SalePrice.
- GrLivArea strongly influences house price.
- Several features contained significant missing values.

---

# Phase 3: Feature Engineering

The following feature engineering techniques were applied.

### Encoding

- Label Encoding
- One-Hot Encoding

### Feature Scaling

- StandardScaler

### Skewness Handling

Applied log transformation using:

```
np.log1p()
```

Highly skewed numerical columns were transformed.

### Feature Selection

Correlation analysis was performed.

Top correlated features:

- OverallQual
- GrLivArea
- GarageCars
- GarageArea
- TotalBsmtSF

---

# Phase 4: Model Training

Multiple regression algorithms were trained.

Models Used

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor
4. Gradient Boosting Regressor
5. XGBoost Regressor
6. LightGBM
7. Catboost

Training Process

- Train-Test Split
- Feature Scaling
- Model Training
- Prediction
- Performance Evaluation

---
# Prediction Page

![Prediction Page](ss_image/s2.png)
# Phase 5: Model Evaluation

The following metrics were used.

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

## Model Comparison

| Model | MAE | RMSE | R² Score |
|--------|------|------|-----------|
| Linear Regression | 15100.268756| 21431.638655| 0.855598|
| Decision Tree | 22403.885714| 32546.308937| 0.666984|
| Random Forest | 13789.298214| 20474.826468|0.868204 |
| Gradient Boosting | 13022.987317|18736.201139 |0.889637 |
| XGBoost |13791.554688 |20234.368386 | 0.871282|
|CatBoost	|11392.195621	|2.777812e+08	|16666.769874	|0.912670

## Best Performing Model

Model Name:
- CatBoost Regressor

Reason

- Highest R² Score
- Lowest RMSE
- Better prediction accuracy compared to other models

---

# Flask Application

The Flask application allows users to:

- Enter house features
- Predict house prices
- View prediction results instantly

---

# Reports Generated

The project includes the following reports:

- Exploratory Data Analysis Report
- Model Evaluation Report
- Prediction Report
- Final Project Documentation

---

# Visualizations Included

The project contains visualizations such as:

- Correlation Heatmap
- Missing Value Chart
- Feature Distribution
- SalePrice Distribution
- Scatter Plots
- Box Plots
- Feature Importance Graph
- Model Comparison Graph

---

# Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Flask
- Joblib

---

# Conclusion

The dataset was successfully cleaned and preprocessed before training multiple regression models.

Among all trained models, **Random Forest Regressor** achieved the best overall performance with the highest prediction accuracy and lowest prediction error.

The trained model was integrated into a Flask web application for real-time house price prediction.

---

