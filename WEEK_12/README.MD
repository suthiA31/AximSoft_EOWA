# AI Customer Intelligence Platform

## 1. Project Overview

The **AI Customer Intelligence Platform** is a lightweight, locally deployable AI system designed to combine traditional customer analytics, machine learning, explainable AI, customer-support text analysis, semantic search, Retrieval-Augmented Generation (RAG), and a small local Large Language Model (LLM).

The platform uses the **IBM Telco Customer Churn dataset** for customer analytics and churn prediction, together with a **customer-support ticket dataset** for NLP, semantic search, and knowledge retrieval.

The system is designed for **CPU-first execution on a low-resource laptop** without requiring paid cloud AI services, dedicated GPUs, or large language models.

The final application provides:

* Customer analytics and dashboards
* Customer profile lookup
* Churn prediction
* SHAP-based explainability
* Customer-support NLP analysis
* Semantic search
* Knowledge-base retrieval
* RAG-based responses
* Local LLM responses
* Tool-based AI workflows
* Simple customer intelligence agent
* GenAI evaluation
* Resource benchmarking
* Flask web interface

---

## 2. Research Question

> **Can a lightweight, locally deployable AI system combine traditional customer analytics, machine learning, explainable AI, semantic retrieval, and a small local LLM to provide reliable and resource-efficient customer intelligence without relying on paid cloud AI services?**

---

## 3. Objectives

The main objectives of the project are to:

1. Perform exploratory analysis of customer data.
2. Use SQL for structured customer analytics.
3. Preprocess and engineer customer-level features.
4. Build churn prediction models.
5. Compare baseline and ensemble machine learning models.
6. Improve the selected model using class weighting, cross-validation, tuning, and threshold adjustment.
7. Provide explainable churn predictions using SHAP.
8. Analyze customer-support text using NLP.
9. Build TF-IDF-based ticket classification.
10. Generate sentence embeddings for semantic search.
11. Build a local FAISS vector database.
12. Create a customer-support knowledge base.
13. Implement Retrieval-Augmented Generation.
14. Use a small local instruction-tuned LLM.
15. Compare different prompt strategies.
16. Integrate SQL, ML, SHAP, RAG, and LLM components.
17. Implement tool calling.
18. Build a simple customer intelligence agent.
19. Evaluate GenAI responses.
20. Benchmark resource usage.
21. Deploy the complete workflow through Flask.

---

# 4. System Architecture

```text
                    CUSTOMER DATA
                         |
                         v
                  Exploratory Data Analysis
                         |
                         v
                    SQL Analytics
                         |
                         v
                 Data Preprocessing
                         |
                         v
                 Feature Engineering
                         |
                         v
              Machine Learning Models
                         |
              +----------+----------+
              |                     |
              v                     v
        Churn Prediction          SHAP
              |                 Explainability
              |                     |
              +----------+----------+
                         |
                         v
                Customer Intelligence
                         |
                         |
       CUSTOMER SUPPORT TICKET DATA
                         |
                         v
                    NLP Cleaning
                         |
                         v
                 TF-IDF Classification
                         |
                         v
                 Sentence Embeddings
                         |
                         v
                    FAISS Search
                         |
                         v
                  Knowledge Base
                         |
                         v
                       RAG
                         |
                         v
                  Local Small LLM
                         |
                         v
                 Tool Calling / Agent
                         |
                         v
                  Flask Web Application
```

---

# 5. Datasets

## 5.1 IBM Telco Customer Churn Dataset

The customer dataset contains approximately **7,043 customer records** and includes information such as:

* Customer ID
* Gender
* Senior citizen status
* Partner
* Dependents
* Tenure
* Phone service
* Internet service
* Contract
* Payment method
* Monthly charges
* Total charges
* Churn

The `Churn` column is used as the prediction target.

`customerID` is treated as an identifier rather than a predictive feature.

## 5.2 Customer Support Tickets Dataset

The support-ticket dataset contains approximately **8,469 records** and includes:

* Ticket ID
* Customer information
* Product purchased
* Ticket type
* Ticket subject
* Ticket description
* Ticket status
* Resolution
* Ticket priority
* Ticket channel
* Response information
* Customer satisfaction

The text fields are used for NLP and semantic search.

`Resolution` is not used as a classification input because it can introduce leakage and is unavailable for some unresolved tickets.

---

# 6. Notebook Workflow

The project is implemented through a sequence of notebooks.

## Notebook 01: EDA

Performs:

* Dataset loading
* Dataset dimensions
* Data types
* Missing-value analysis
* Duplicate analysis
* Unique-value analysis
* Statistical summaries
* Churn distribution
* Contract analysis
* Payment-method analysis
* Internet-service analysis
* Tenure analysis
* Monthly-charge analysis
* Correlation analysis
* Customer segmentation
* Service analysis
* Outlier inspection

The processed customer dataset is saved for later stages.

---

## Notebook 02: SQL Analytics

A local **SQLite** database is created for structured customer analysis.

Queries include:

* Total customers
* Churned customers
* Churn rate
* Churn by contract
* Churn by payment method
* Churn by internet service
* Average monthly charges
* Average total charges
* High-value customers
* High-risk groups
* Long-tenure customers
* Service segments
* Revenue-related analysis
* Customer profile lookup

The database is stored locally and is later used by the Flask application.

---

## Notebook 03: Data Preprocessing and Feature Engineering

The preprocessing pipeline handles:

* Numeric conversion
* Missing values
* Identifier removal
* Categorical encoding
* Numerical scaling
* Train/test splitting
* Class balancing preparation

Additional engineered features include:

```text
NewCustomer
LongTermCustomer
ChargeToTenure
HighMonthlyCharge
HighValueHighRisk
```

The preprocessing pipeline is saved using Joblib for reuse in the Flask application.

---

## Notebook 04: ML Baseline and Ensemble Models

The following models are evaluated:

### Baseline Models

* Logistic Regression
* Decision Tree
* K-Nearest Neighbors

### Ensemble Models

* Random Forest
* Gradient Boosting
* XGBoost

Evaluation metrics include:

* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC
* PR-AUC
* Confusion Matrix

Special attention is given to churn recall, precision, F1-score, ROC-AUC, PR-AUC, and computational efficiency.

---

## Notebook 05: Model Improvement

The selected Logistic Regression model is improved using:

* Class weighting
* Stratified cross-validation
* Randomized hyperparameter search
* Regularization tuning
* Threshold adjustment

A decision threshold of **0.55** was selected based on the evaluation performed in the project.

The improved model is saved for reuse by the application.

---

# 7. SHAP Explainability

## Notebook 06

Explainable AI is implemented using **SHAP**.

The project uses the saved **XGBoost tree-based model** with `TreeExplainer`.

SHAP provides:

* Global feature importance
* SHAP summary analysis
* Individual customer explanations
* Positive churn contributors
* Negative churn contributors
* Individual contribution values

The system separates prediction and explanation components:

```text
Improved Logistic Regression
        |
        v
Churn Probability


XGBoost
   |
   v
TreeExplainer
   |
   v
SHAP Explanation
```

This allows the application to show both the predicted risk and the factors contributing to the model explanation.

---

# 8. Customer Support NLP

## Notebook 07

The customer-support ticket dataset is processed using NLP techniques.

Text preprocessing includes:

* Lowercasing
* URL removal
* Number removal
* Punctuation removal
* Tokenization
* Stopword removal
* Short-token removal
* Word-count analysis

Additional analysis includes:

* Word frequency
* Bigram analysis
* Text statistics
* Ticket-type classification

---

# 9. TF-IDF Classification

TF-IDF is used to convert customer-support text into numerical features.

The classification model uses:

* TF-IDF
* Unigrams and bigrams
* Logistic Regression

The target is `Ticket Type`.

The trained vectorizer and classifier are saved for reuse.

---

# 10. Sentence Embeddings and FAISS

## Notebook 08

The project uses:

```text
all-MiniLM-L6-v2
```

to generate lightweight sentence embeddings.

The embeddings are stored in a local **FAISS** vector index.

Semantic search allows the system to retrieve support tickets based on meaning rather than exact keyword matching.

The embedding dimension is approximately:

```text
384
```

The FAISS index uses normalized embeddings and inner-product similarity.

---

# 11. Knowledge Base

## Notebook 09

A local knowledge base is created using text documents covering areas such as:

* Billing policy
* Cancellation policy
* Contract policy
* Retention policy
* Support FAQs
* Business rules
* Service FAQs

The documents are split into chunks and converted into embeddings.

FAISS is then used to retrieve relevant knowledge.

The knowledge base is separate from structured SQL customer information.

---

# 12. Retrieval-Augmented Generation

## Notebook 09 and 10

The RAG pipeline follows:

```text
User Question
      |
      v
Question Embedding
      |
      v
FAISS Knowledge Search
      |
      v
Top Relevant Documents
      |
      v
Context Construction
      |
      v
Local LLM
      |
      v
Grounded Response
```

The system retrieves approximately **3 to 5 relevant knowledge chunks** before generating a response.

The retrieved context is provided to the local LLM to reduce unsupported answers.

---

# 13. Local Small LLM

The project uses a lightweight local instruction-tuned model:

```text
Qwen/Qwen2.5-1.5B-Instruct
```

The model runs locally using Hugging Face Transformers.

The LLM is responsible for:

* Understanding user questions
* Combining verified information
* Summarizing customer information
* Generating grounded responses
* Explaining retrieved information

The LLM does **not** independently calculate customer churn probability.

Verified information is supplied from SQL, ML, SHAP, and RAG components.

---

# 14. Prompt Engineering

## Notebook 11

Several prompt strategies are evaluated:

* Basic prompt
* Role-based prompt
* Context-based prompt
* Grounded RAG prompt
* Customer intelligence prompt
* Final production prompt

The final prompting strategy emphasizes:

* Correctness
* Relevance
* Evidence
* Groundedness
* Consistency
* Avoidance of hallucinated customer information

---

# 15. Integrated Customer Intelligence

## Notebook 12

The integrated workflow combines:

```text
Customer ID
     |
     v
SQLite Customer Profile
     |
     v
Churn Prediction
     |
     v
SHAP Explanation
     |
     v
Knowledge Base Retrieval
     |
     v
Local LLM
     |
     v
Customer Intelligence Response
```

The system provides the LLM with verified information rather than allowing it to invent customer details or prediction results.

---

# 16. Tool Calling

## Notebook 13

The project implements simple tool-based workflows.

The main tools are:

```python
get_customer_profile(customer_id)
```

Retrieves structured customer information.

```python
predict_churn(customer_id)
```

Returns churn probability and risk classification.

```python
get_shap_explanation(customer_id)
```

Returns important SHAP contributors.

```python
search_knowledge_base(query)
```

Retrieves relevant knowledge-base information.

The tools provide verified information to the AI workflow.

---

# 17. Simple Agent Workflow

## Notebook 14

A lightweight single-agent architecture is implemented.

The agent:

1. Understands the user question.
2. Identifies the required information.
3. Selects appropriate tools.
4. Executes the tools.
5. Collects verified results.
6. Builds grounded context.
7. Sends the context to the local LLM.
8. Generates the final response.

The system intentionally avoids complex multi-agent frameworks and long-running agent chains.

---

# 18. GenAI Evaluation

## Notebook 15

The GenAI system is evaluated using a set of **12 test questions** covering:

* Customer Lookup
* Churn
* Churn Explanation
* Risk Factors
* Policy
* Knowledge Base
* Combined Questions
* Groundedness

Evaluation dimensions include:

* Correctness
* Relevance
* Groundedness
* Evidence
* Consistency
* Hallucination
* Response Time

The evaluation results are stored in the processed-data directory.

---

# 19. Resource Benchmarking

## Notebook 16

The system is benchmarked for lightweight local deployment.

Measured components include:

* Model loading time
* ML inference time
* Embedding model loading
* Embedding generation
* FAISS search
* Local LLM loading
* LLM inference
* End-to-end agent response
* Approximate RAM usage

This helps evaluate whether the complete architecture is practical on a CPU-based low-resource environment.

---

# 20. Flask Application

The final Flask application provides four main pages.

## Dashboard

Displays:

* Customer statistics
* Churn information
* Contract distribution
* Internet-service information
* Customer analytics charts
* Key project metrics

## Customer Profile

Allows the user to search using Customer ID.

Displays:

* Customer information
* Tenure
* Contract
* Payment method
* Internet service
* Monthly charges
* Total charges
* Services
* Churn probability
* Risk level

## Explainable AI

Displays:

* Churn probability
* Risk level
* Important positive SHAP contributors
* Important negative SHAP contributors
* SHAP contribution overview

## Ask AI

Allows users to ask natural-language customer intelligence questions.

The assistant can combine:

* SQL customer information
* ML churn prediction
* SHAP explanations
* Knowledge-base retrieval
* Local LLM generation

---

# 21. Project Structure

```text
ai_customer_intelligence/
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── knowledge_base/
│   └── customer_intelligence.db
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_sql_analysis.ipynb
│   ├── 03_preprocessing.ipynb
│   ├── 04_ml_models.ipynb
│   ├── 05_model_improvement.ipynb
│   ├── 06_shap_explainability.ipynb
│   ├── 07_nlp_ticket_analysis.ipynb
│   ├── 08_embeddings_faiss.ipynb
│   ├── 09_knowledge_base_rag.ipynb
│   ├── 10_local_llm_rag.ipynb
│   ├── 11_prompt_engineering.ipynb
│   ├── 12_integrated_customer_intelligence.ipynb
│   ├── 13_tool_calling.ipynb
│   ├── 14_simple_agent_workflow.ipynb
│   ├── 15_genai_evaluation.ipynb
│   └── 16_resource_benchmarking.ipynb
│
├── models/
│   ├── preprocessor.pkl
│   ├── improved_logistic_regression.pkl
│   ├── xgboost_churn_model.pkl
│   ├── shap_explainer.pkl
│   ├── tfidf_vectorizer.pkl
│   └── ticket_type_classifier.pkl
│
├── vector_store/
│   ├── knowledge_faiss.index
│   ├── knowledge_metadata.pkl
│   └── ticket_faiss.index
│
├── Flask/
│   ├── app.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── customer.html
│   │   ├── shap.html
│   │   └── assistant.html
│   │
│   └── static/
│       ├── style.css
│       └── js/
│           └── app.js
│
├── requirements.txt
└── README.md
```

---

# 22. Technologies Used

### Programming

* Python
* SQL
* HTML
* CSS
* JavaScript

### Data Analysis

* Pandas
* NumPy
* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* XGBoost

### Explainable AI

* SHAP

### NLP

* NLTK
* TF-IDF
* Scikit-learn

### Embeddings

* Sentence Transformers
* `all-MiniLM-L6-v2`

### Vector Search

* FAISS

### Generative AI

* Hugging Face Transformers
* PyTorch
* Qwen 1.5B Instruct

### Database

* SQLite

### Web Application

* Flask
* HTML
* CSS
* JavaScript

### Model and Artifact Storage

* Joblib
* Pickle

---

# 23. Installation

Create and activate a Python virtual environment:

```bash
python -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

The local LLM and embedding model may require an internet connection during their first download. After the models are available locally, inference can be performed locally.

---

# 24. Running the Application

Navigate to the Flask directory:

```bash
cd Flask
```

Start the application:

```bash
python app.py
```

Open the application in a browser:

```text
http://127.0.0.1:5000/
```

Available pages:

```text
/
```

Dashboard

```text
/customer
```

Customer Profile

```text
/explain
```

SHAP Explainable AI

```text
/assistant
```

Ask AI

---

# 25. Example Workflow

A typical customer intelligence request follows this process:

```text
User:
"What is the churn risk for customer 7590-VHVEG?"
             |
             v
Customer Profile Tool
             |
             v
SQLite
             |
             v
Customer Information
             |
             v
Churn Prediction Tool
             |
             v
Churn Probability
             |
             v
SHAP Tool
             |
             v
Important Risk Factors
             |
             v
Knowledge Base
             |
             v
Relevant Business Information
             |
             v
Local LLM
             |
             v
Grounded Customer Intelligence Response
```

---

# 26. Design Principles

The project follows several important design principles:

### Local First

The architecture is designed to run locally without paid cloud AI APIs.

### Lightweight

Small models and CPU-friendly components are preferred.

### Explainable

The system provides SHAP-based explanations rather than only displaying a prediction.

### Grounded

The LLM receives verified customer and business information from system components.

### Modular

Each component can be developed, tested, and evaluated independently.

### Reusable

Models, preprocessors, vector indexes, and configurations are saved for use by the Flask application.

### Separation of Responsibilities

Structured numerical information is retrieved through SQL and ML components, while unstructured business knowledge is retrieved through the RAG pipeline.

---

# 27. Limitations

The system has several limitations:

* The churn model is based on the available Telco dataset.
* Model performance depends on the original dataset and feature engineering.
* The local LLM has fewer capabilities than large cloud-based models.
* CPU-based LLM inference can be relatively slow.
* Knowledge-base answers depend on the quality and coverage of the stored documents.
* SHAP explanations describe model behavior and should not automatically be interpreted as causal relationships.
* The GenAI evaluation uses a compact set of 12 test questions.
* The platform is intended as an academic and demonstration system rather than a production customer-management platform.

---

# 28. Expected Outcome

The completed platform demonstrates how conventional analytics and modern AI techniques can be combined into a single lightweight customer intelligence system.

The final system connects:

```text
EDA
 ↓
SQL
 ↓
Preprocessing
 ↓
Feature Engineering
 ↓
Machine Learning
 ↓
SHAP
 ↓
NLP
 ↓
TF-IDF
 ↓
Embeddings
 ↓
FAISS
 ↓
Knowledge Base
 ↓
RAG
 ↓
Local LLM
 ↓
Tool Calling
 ↓
Simple Agent
 ↓
Evaluation
 ↓
Benchmarking
 ↓
Flask Application
```

The resulting platform provides a complete example of **resource-efficient, locally deployable customer intelligence using traditional machine learning, explainable AI, retrieval-based AI, and a small local language model**.

---

# 29. Conclusion

The **AI Customer Intelligence Platform** demonstrates an end-to-end architecture for combining structured customer analytics with unstructured customer-support intelligence.

Rather than depending entirely on a large language model, the system uses specialized components for each task:

* SQLite handles structured customer information.
* Machine learning predicts churn.
* SHAP explains model predictions.
* NLP analyzes support tickets.
* TF-IDF performs text classification.
* Sentence Transformers generate semantic representations.
* FAISS performs local semantic retrieval.
* RAG retrieves relevant business knowledge.
* A small local LLM generates grounded natural-language responses.
* Tool calling connects these capabilities.
* Flask provides an accessible user interface.

This architecture demonstrates how AI customer intelligence can be implemented in a **modular, explainable, resource-conscious, and locally deployable environment**.
