# ⚡ End-to-End Electricity Demand Forecasting using Deep Learning

## 📌 Project Overview

This project develops an end-to-end **electricity demand forecasting system** using historical hourly electricity consumption data and deep learning techniques.

The project covers the complete machine learning workflow:

* Data Understanding
* Time-Series Preprocessing
* Exploratory Data Analysis
* Baseline Forecasting
* Deep Learning Model Development
* Model Improvement
* Forecast Validation
* Model Evaluation
* Flask Forecasting Dashboard
* Git and GitHub Integration

The main objective is to predict future electricity demand from historical demand patterns and compare different deep learning architectures to identify the best-performing forecasting model.

---

# 📊 Dataset

### Hourly Energy Consumption - PJM

The project uses the **Hourly Energy Consumption - PJM** dataset from Kaggle.

Dataset:

https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption

The dataset contains hourly electricity consumption records for different PJM regions.

The processed project dataset used for modelling is:

```text
pjm_processed.csv
```

### Main Data Columns

| Column      | Description                         |
| ----------- | ----------------------------------- |
| `timestamp` | Date and time of electricity demand |
| `demand`    | Hourly electricity consumption      |

---

# 🏗️ Project Architecture

```text
Raw Electricity Data
        │
        ▼
┌─────────────────────┐
│ Phase 1             │
│ Data Understanding  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Phase 2             │
│ Preprocessing       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Phase 3             │
│ EDA                 │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Phase 4             │
│ Baseline Models     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Phase 5             │
│ Deep Learning       │
│ RNN/LSTM/GRU/BiLSTM│
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Phase 6             │
│ Model Improvement   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Phase 7             │
│ Forecast Validation │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Phase 8             │
│ Model Evaluation    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Phase 9             │
│ Flask Dashboard     │
└─────────────────────┘
```

---

# 🔹 Phase 1 - Data Understanding

The first phase focuses on understanding the electricity demand time series.

### Activities

* Analyze timestamps
* Check time intervals
* Identify missing records
* Identify duplicate records
* Analyze electricity demand trends
* Identify daily seasonality
* Identify weekly seasonality
* Identify monthly and yearly patterns
* Identify abnormal demand periods

### Visualizations

* Time-series plot
* Daily demand pattern
* Weekly demand pattern
* Monthly trend
* Demand distribution
* Seasonal decomposition

---

# 🔹 Phase 2 - Time-Series Preprocessing

The raw data is prepared for machine learning and deep learning.

### Preprocessing Steps

1. Convert timestamp to datetime.
2. Sort records chronologically.
3. Set timestamp as the dataframe index.
4. Check missing timestamps.
5. Check missing demand values.
6. Check duplicate records.
7. Detect abnormal demand values.
8. Create time-based features.
9. Create lag features.
10. Create rolling statistics.
11. Scale the demand values.

### Time-Based Features

```text
Hour
Day
Week
Month
Day of Week
Weekend / Weekday
```

### Lag Features

Historical demand values can be used as input features.

Examples:

```text
Lag 1
Lag 24
Lag 48
Lag 168
```

where:

```text
24 hours  = previous day
168 hours = previous week
```

### Rolling Features

Rolling statistics capture recent demand behavior.

Examples:

```text
Rolling Mean - 24 hours
Rolling Standard Deviation - 24 hours

Rolling Mean - 168 hours
Rolling Standard Deviation - 168 hours
```

`shift(1)` is applied before calculating rolling statistics to prevent the current target value from leaking into the feature.

---

# 🔹 Phase 3 - Exploratory Data Analysis

EDA is performed to understand electricity demand behavior.

### Analysis

* Hourly demand patterns
* Daily demand patterns
* Weekly seasonality
* Monthly seasonality
* Annual patterns
* Peak demand periods
* Off-peak demand periods
* Lag relationships
* Rolling mean
* Rolling standard deviation

### Visualizations

```text
Hourly Demand Profile
Weekly Demand Profile
Hour vs Day Heatmap
Rolling Mean / Standard Deviation
Autocorrelation Plot
Seasonal Decomposition
Demand Distribution
```

These visualizations help identify recurring demand patterns that can be learned by the forecasting models.

---

# 🔹 Phase 4 - Baseline Forecasting Models

Before using deep learning, simple forecasting approaches are implemented.

The purpose is to establish a baseline.

### Baseline Models

#### 1. Naive Forecast

Uses the most recent demand value as the prediction.

```text
Previous Demand → Future Demand
```

#### 2. Moving Average

Uses the average of recent observations.

#### 3. Previous-Day Forecast

Uses demand from the corresponding time on the previous day.

```text
Current Monday 10 AM
        ↓
Previous Monday 10 AM
```

#### 4. Previous-Week Forecast

Uses demand from the corresponding time during the previous week.

```text
Current Monday 10 AM
        ↓
Previous Monday 10 AM
```

The baseline results are compared with deep learning models to determine whether deep learning provides meaningful improvement.

---

# 🔹 Phase 5 - Deep Learning Models

Deep learning models are developed to forecast future electricity demand.

The models use historical sequences to predict future demand.

### Forecasting Setup

Example:

```text
Previous 24 Hours
       ↓
    RNN/LSTM/GRU
       ↓
Next 24 Hours
```

Different sequence lengths are also tested:

```text
24 Hours  → Next 24 Hours

48 Hours  → Next 24 Hours

168 Hours → Next 24 Hours
```

---

## 🧠 Sliding Window

A sliding-window approach is used to create sequences.

For:

```text
sequence_length = 24
forecast_horizon = 24
```

the model receives:

```text
X = Previous 24 Hours
```

and learns to predict:

```text
y = Next 24 Hours
```

The window then moves forward and creates another training sample.

---

# 🤖 Models

## RNN

A Simple RNN is used as the basic recurrent model.

Architecture:

```text
Input
  ↓
SimpleRNN(64)
  ↓
Dense(24)
  ↓
24-Hour Forecast
```

---

## LSTM

LSTM is used to capture longer-term dependencies in the time series.

Architecture:

```text
Input
  ↓
LSTM(64)
  ↓
Dense(24)
  ↓
24-Hour Forecast
```

---

## GRU

GRU is another gated recurrent architecture.

Architecture:

```text
Input
  ↓
GRU(64)
  ↓
Dense(24)
  ↓
24-Hour Forecast
```

---

## Bidirectional LSTM

Bidirectional LSTM processes the input sequence in both directions.

Architecture:

```text
Input
  ↓
Bidirectional
      ↓
   LSTM(64)
      ↓
   Dense(24)
      ↓
24-Hour Forecast
```

---

# 🔹 Phase 6 - Model Improvement

After developing the initial models, multiple experiments are performed to improve forecasting performance.

### Experiments

* Different sequence lengths
* Additional lag features
* Rolling features
* Feature scaling
* Dropout
* Batch Normalization
* Different optimizers
* Learning-rate scheduling
* Early stopping
* Batch-size tuning
* Number of layers
* Number of neurons
* Hyperparameter tuning

---

## Learning Rate Scheduling

`ReduceLROnPlateau` is used to reduce the learning rate when validation loss stops improving.

Example:

```python
ReduceLROnPlateau(
    monitor="val_loss",
    factor=0.5,
    patience=3,
    min_lr=1e-6
)
```

This allows the model to make smaller weight updates when learning reaches a plateau.

---

## Optimizer Comparison

Different optimizers can be compared:

```text
Adam
RMSprop
```

The optimizer that provides better validation performance can be selected for further experimentation.

---

# 🔹 Phase 7 - Forecast Validation

The dataset is divided chronologically to prevent future information from entering the training process.

### Data Split

```text
Historical Data
       │
       ├─────────────── Training
       │
       ├─────────────── Validation
       │                 30 / 60 Days
       │
       └─────────────── Test
                         Final 20%
```

### Validation

A recent 30-day or 60-day period is kept separate from final model training.

For 30 days:

```text
30 × 24 = 720 hours
```

The model generates predictions for this unseen period and the predictions are compared with the actual electricity demand.

---

## Validation Visualizations

* Actual vs Forecast
* 30-Day Forecast
* 60-Day Forecast
* Daily Error
* Peak Demand Error
* Forecast Error Distribution

---

## Peak Demand Error

Peak demand is defined using the 90th percentile of actual demand.

```python
peak_threshold = np.percentile(
    actual_30,
    90
)
```

Only high-demand periods are selected and their MAE is calculated.

This determines whether the model performs well during important peak-demand periods.

---

# 🔹 Phase 8 - Model Evaluation

All models are evaluated using multiple metrics.

| Metric | Meaning                          |
| ------ | -------------------------------- |
| MAE    | Mean Absolute Error              |
| MSE    | Mean Squared Error               |
| RMSE   | Root Mean Squared Error          |
| MAPE   | Mean Absolute Percentage Error   |
| R²     | Coefficient of Determination     |
| Bias   | Systematic over/under prediction |

### Interpretation

**MAE**

Lower is better.

```text
Average absolute forecasting error
```

**RMSE**

Lower is better.

RMSE gives more importance to larger errors.

**MAPE**

Lower is better.

Measures error as a percentage.

**R²**

Higher is better.

Shows how much variation in demand is explained by the model.

**Bias**

Shows whether the model tends to:

```text
Overpredict
```

or

```text
Underpredict
```

---

# 📊 Model Comparison

The final models are compared using a consolidated results table.

| Model          | MAE | MSE | RMSE | MAPE | R² | Bias |
| -------------- | --: | --: | ---: | ---: | -: | ---: |
| Naive          |   - |   - |    - |    - |  - |    - |
| Moving Average |   - |   - |    - |    - |  - |    - |
| RNN            |   - |   - |    - |    - |  - |    - |
| LSTM           |   - |   - |    - |    - |  - |    - |
| GRU            |   - |   - |    - |    - |  - |    - |
| Bi-LSTM        |   - |   - |    - |    - |  - |    - |

> Replace the values above with the final experimental results.

The final model is selected based primarily on validation and test performance rather than training performance alone.

---

# 🔹 Phase 9 - Forecasting Dashboard

The final forecasting system is integrated into a Flask web application.

### Technologies

```text
Flask
Bootstrap
HTML
CSS
JavaScript
Chart.js / Plotly
```

---

## Dashboard

The dashboard displays:

* Current/latest demand
* Historical consumption
* Forecast summary
* Model performance

---

## Forecast Page

Users can:

* Select forecasting horizon
* Generate future demand
* View forecast values
* View forecast intervals where implemented

---

## Analytics

The analytics section provides:

* Actual vs Forecast
* Daily trends
* Weekly trends
* Monthly trends
* Peak demand analysis
* Forecast errors
* Model comparison

---

## Validation Page

Users can select:

```text
30 Days
60 Days
```

The page displays:

* Actual demand
* Predicted demand
* MAE
* RMSE
* MAPE
* Forecast performance charts

---

# 📁 Project Structure

```text
Week_10/
│
├── Phase_01/
│   └── data_understanding.ipynb
│
├── Phase_02/
│   └── preprocessing.ipynb
│
├── Phase_03/
│   └── EDA.ipynb
│
├── Phase_04/
│   └── baseline_models.ipynb
│
├── Phase_05/
│   └── deep_learning_models.ipynb
│
├── Phase_06/
│   └── model_improvement.ipynb
│
├── Phase_07/
│   └── forecast_validation.ipynb
│
├── Phase_08/
│   └── model_evaluation.ipynb
│
├── Flask/
│   ├── app.py
│   ├── templates/
│   ├── static/
│   └── model/
│
├── data/
│   └── pjm_processed.csv
│
├── documentation_output/
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

---

# 🛠️ Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
```

Navigate to the project:

```bash
cd Week_10
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

### Linux / Ubuntu

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

The major libraries used in the project are:

```text
Python
Pandas
NumPy
Scikit-learn
TensorFlow
Keras
Matplotlib
Seaborn
Flask
Bootstrap
python-docx
```

---

# 🚀 Running the Flask Dashboard

Navigate to the Flask application:

```bash
cd Flask
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Run:

```bash
python app.py
```

The Flask application can then be accessed through the local development server.

---

# 🔀 Git and GitHub

Git is used for version control and project collaboration.

### Recommended Branches

```text
main
│
├── feature/preprocessing
├── feature/modelling
├── feature/model-improvement
└── feature/dashboard
```

### Example Commit Messages

```text
Implement time-series preprocessing

Add baseline forecasting models

Implement RNN LSTM GRU and Bi-LSTM models

Add model improvement experiments

Add forecast validation pipeline

Implement Flask forecasting dashboard

Add project documentation
```

---

# 📈 Final Outcome

The final outcome of this project is an end-to-end electricity demand forecasting application that:

1. Processes historical electricity demand data.
2. Identifies time-series patterns.
3. Creates forecasting sequences.
4. Trains baseline forecasting models.
5. Trains RNN, LSTM, GRU, and Bi-LSTM models.
6. Improves the models using optimization techniques.
7. Validates forecasts on unseen chronological periods.
8. Evaluates models using multiple metrics.
9. Selects the best-performing forecasting model.
10. Provides an interactive Flask dashboard for forecasting and analytics.

---

# 🎯 Conclusion

This project demonstrates how deep learning can be applied to electricity demand forecasting using historical time-series data.

The complete workflow combines time-series preprocessing, exploratory data analysis, feature engineering, baseline forecasting, recurrent neural networks, model optimization, chronological validation, performance evaluation, and web deployment.

The final Flask dashboard provides a practical interface for viewing electricity demand patterns, generating forecasts, analyzing model performance, and evaluating forecasting errors.

The best forecasting model is selected based on its ability to generalize to unseen validation and test periods while maintaining low forecasting error and strong predictive performance.

---

# 👨‍💻 Technologies Used

```text
Python
Pandas
NumPy
Scikit-learn
TensorFlow
Keras
Matplotlib
Seaborn
Flask
Bootstrap
Git
GitHub
```

---

# 📌 Project Status

```text
Phase 1  → Data Understanding       ✅
Phase 2  → Preprocessing            ✅
Phase 3  → EDA                      ✅
Phase 4  → Baseline Models          ✅
Phase 5  → Deep Learning            ✅
Phase 6  → Model Improvement        ✅
Phase 7  → Forecast Validation      🔄
Phase 8  → Model Evaluation         🔄
Phase 9  → Flask Dashboard          🔄
```

> Update the status icons as each phase is finalized.
