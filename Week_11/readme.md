[1:07 PM] Keerthi Karuppusamy
# IMDB Sentiment Analysis Using Deep Learning
 
## Project Overview
 
This project performs **sentiment analysis on IMDB movie reviews**.
 
The system predicts whether a movie review is:
 
* Positive

* Negative
 
Different Deep Learning models are trained and compared:
 
* ANN

* Simple RNN

* LSTM

* GRU

* Bidirectional LSTM (BiLSTM)
 
The final project also includes a **Flask web application** for predicting sentiment from user-entered movie reviews.
 
---
 
## Dataset
 
**File:** `IMDB Dataset.csv`
 
The dataset contains two columns:
 
| Column      | Description          |

| ----------- | -------------------- |

| `review`    | Movie review text    |

| `sentiment` | Positive or Negative |
 
---
 
## Project Structure
 
```text

week_09/

│

├── IMDB Dataset.csv

│

├── phase1.ipynb

├── phase2.ipynb

├── phase3.ipynb

├── phase4.ipynb

│

├── phase5.ipynb

├── phase5_rnn.ipynb

├── phase5_lstm.ipynb

├── phase5_gru.ipynb

├── phase5_bilstm.ipynb

│

├── phase6.ipynb

├── Phase7.ipynb

│

├── artifacts/

├── models/

│

└── flask_app/

```
 
---
 
## Project Phases
 
### Phase 1 - Data Understanding
 
* Load the IMDB dataset

* Check dataset information

* Check missing values

* Check duplicate values

* Analyze sentiment distribution

* Analyze review length and word count
 
### Phase 2 - Data Preprocessing
 
* Clean text data

* Prepare movie reviews for further processing
 
### Phase 3 - Feature Preparation
 
* Tokenization

* Convert text into sequences

* Padding sequences

* Prepare training, validation, and test data

* Save preprocessing artifacts
 
### Phase 4 - Model Development
 
Build Deep Learning models:
 
* ANN

* RNN

* LSTM

* GRU

* BiLSTM
 
### Phase 5 - Model Training
 
Train and evaluate the different models.
 
Separate notebooks are available for:
 
* RNN

* LSTM

* GRU

* BiLSTM
 
### Phase 6 - Model Evaluation
 
Analyze and compare the trained models.
 
### Phase 7 - Final Analysis
 
Perform the final project analysis and summarize the results.
 
---
 
## Technologies Used
 
* Python

* Pandas

* NumPy

* NLTK

* TensorFlow

* Keras

* Scikit-learn

* Matplotlib

* Seaborn

* Flask
 
Flask Application
 
The project includes a Flask application located in:
 
flask_app/
 
The Flask application is used to provide a practical interface for the trained sentiment analysis system.
 
The general prediction flow is:
 
User enters movie review

          │

          ▼

Flask Application

          │

          ▼

Text Preprocessing

          │

          ▼

Tokenization

          │

          ▼

Sequence Preparation

          │

          ▼

Trained Deep Learning Model

          │

          ▼

Sentiment Prediction

          │

          ▼

Positive / Negative Result
 
## Project Workflow
 
```text

IMDB Reviews

     ↓

Data Understanding

     ↓

Text Preprocessing

     ↓

Tokenization

     ↓

Sequence Preparation

     ↓

Train Deep Learning Models

     ↓

ANN / RNN / LSTM / GRU / BiLSTM

     ↓

Model Evaluation

     ↓

Model Comparison

     ↓

Flask Deployment

     ↓

Sentiment Prediction

 
