from flask import Flask, render_template, request, jsonify
import os
import sqlite3
import joblib
import json
import numpy as np
import pandas as pd
import shap
import faiss
import torch

from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM


# ============================================================
# FLASK APP
# ============================================================

app = Flask(__name__)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")
MODELS_DIR = os.path.join(BASE_DIR, "models")
VECTOR_DIR = os.path.join(BASE_DIR, "vector_store")

DB_PATH = "/home/aximsoft/Documents/AximSoft_EOWA/WEEK_12/Notebooks/processed/customer_intelligence.db"

CUSTOMER_DATA_PATH = "/home/aximsoft/Documents/AximSoft_EOWA/WEEK_12/Notebooks/processed/telco_eda_processed.csv"


# ============================================================
# LOAD CUSTOMER DATA
# ============================================================

customer_df = pd.read_csv(
    CUSTOMER_DATA_PATH
)

print(
    "Customer dataset loaded:",
    customer_df.shape
)


# ============================================================
# LOAD PREPROCESSOR
# ============================================================

preprocessor = joblib.load(
    "/home/aximsoft/Documents/AximSoft_EOWA/WEEK_12/models/preprocessor.pkl"
)


# ============================================================
# LOAD CHURN MODEL
# ============================================================

churn_model = joblib.load(
    os.path.join(
      "/home/aximsoft/Documents/AximSoft_EOWA/WEEK_12/models/improved_logistic_regression.pkl"
))


# ============================================================
# LOAD XGBOOST FOR SHAP
# ============================================================

xgboost_model = joblib.load(
   "/home/aximsoft/Documents/AximSoft_EOWA/WEEK_12/models/xgboost_churn_model.pkl"
)

shap_explainer = shap.TreeExplainer(
    xgboost_model
)


# ============================================================
# LOAD KNOWLEDGE BASE
# ============================================================

knowledge_index = faiss.read_index(
    "/home/aximsoft/Documents/AximSoft_EOWA/WEEK_12/vector_store/knowledge_faiss.index"
)

knowledge_metadata = joblib.load(
  "/home/aximsoft/Documents/AximSoft_EOWA/WEEK_12/vector_store/knowledge_metadata.pkl"
)


# ============================================================
# LOAD EMBEDDING MODEL
# ============================================================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# ============================================================
# LOCAL LLM
# ============================================================

MODEL_NAME = "Qwen/Qwen2.5-1.5B-Instruct"

tokenizer = None
llm_model = None

print("Local LLM will be loaded only when Ask AI is used.")

def load_local_llm():

    global tokenizer
    global llm_model

    if tokenizer is not None and llm_model is not None:
        return

    print("Loading local LLM...")

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME
    )

    llm_model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float32
    )

    llm_model.eval()

    print("Local LLM loaded successfully.")
# ============================================================
# DATABASE CONNECTION
# ============================================================

import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = "/home/aximsoft/Documents/AximSoft_EOWA/WEEK_12/Notebooks/processed/customer_intelligence.db"
DB_PATH = os.path.abspath(DB_PATH)

print("SQLite database:", DB_PATH)
print("Database exists:", os.path.exists(DB_PATH))


def get_db_connection():

    connection = sqlite3.connect(DB_PATH)

    connection.row_factory = sqlite3.Row

    return connection
# ============================================================
# CUSTOMER PROFILE
# ============================================================

def get_customer_profile(customer_id):

    customer_id = str(customer_id).strip()

    connection = get_db_connection()

    query = """
    SELECT *
    FROM customers
    WHERE TRIM(customerID) = ?
    """

    result = connection.execute(
        query,
        (customer_id,)
    ).fetchone()

    connection.close()

    if result is None:
        print(
            f"Customer not found in SQLite: '{customer_id}'"
        )
        return None

    profile = dict(result)

    print(
        f"Customer found: {profile.get('customerID')}"
    )

    return profile

# ============================================================
# CHURN PREDICTION
# ============================================================

# ============================================================
# FEATURE ENGINEERING
# ============================================================

MONTHLY_CHARGE_THRESHOLD = customer_df["MonthlyCharges"].quantile(0.75)


def prepare_customer_features(customer_row):

    # -----------------------------
    # TotalCharges
    # -----------------------------
    total_charges = customer_row.get("TotalCharges", 0)

    if pd.isna(total_charges):
        total_charges = customer_df["TotalCharges"].median()

    total_charges = float(total_charges)

    # -----------------------------
    # Tenure
    # -----------------------------
    tenure = customer_row.get("tenure", 0)

    if pd.isna(tenure):
        tenure = 0

    tenure = float(tenure)

    # -----------------------------
    # Monthly Charges
    # -----------------------------
    monthly_charges = customer_row.get("MonthlyCharges", 0)

    if pd.isna(monthly_charges):
        monthly_charges = customer_df["MonthlyCharges"].median()

    monthly_charges = float(monthly_charges)

    # -----------------------------
    # Feature engineering
    # -----------------------------
    new_customer = int(tenure <= 6)

    long_term_customer = int(tenure >= 48)

    charge_to_tenure = (
        total_charges / (tenure + 1)
    )

    high_monthly_charge = int(
        monthly_charges >= MONTHLY_CHARGE_THRESHOLD
    )

    high_value_high_risk = int(
        monthly_charges >= MONTHLY_CHARGE_THRESHOLD
        and new_customer == 1
    )

    # -----------------------------
    # Return customer features
    # -----------------------------
    features = customer_row.copy()

    features["TotalCharges"] = total_charges
    features["tenure"] = tenure
    features["MonthlyCharges"] = monthly_charges

    features["NewCustomer"] = new_customer
    features["LongTermCustomer"] = long_term_customer
    features["ChargeToTenure"] = charge_to_tenure
    features["HighMonthlyCharge"] = high_monthly_charge
    features["HighValueHighRisk"] = high_value_high_risk

    return features

def predict_churn(customer_id):

    customer = customer_df[
        customer_df["customerID"].astype(str).str.strip()
        == str(customer_id).strip()
    ]

    if customer.empty:
        return None

    customer_row = customer.iloc[0].copy()

    # Prepare features
    customer_features = prepare_customer_features(customer_row)

    # Convert to DataFrame
    X = pd.DataFrame([customer_features])

    # Remove columns that should not go into model
    X = X.drop(
        columns=["customerID", "Churn"],
        errors="ignore"
    )

    # Transform features
    X_processed = preprocessor.transform(X)

    # XGBoost prediction
    probability = xgboost_model.predict_proba(
        X_processed
    )[0][1]

    probability = float(probability)
    percent = probability * 100

    threshold = 0.55

    if probability >= threshold:
        prediction_label = "High Risk"
    else:
        prediction_label = "Low Risk"

    return {
        "customer_id": str(customer_id),
        "probability": probability,
        "percent": percent,
        "threshold": threshold,
        "prediction": prediction_label
    }
# ============================================================
# SHAP EXPLANATION
# ============================================================

def get_shap_explanation(customer_id, top_n=6):

    # ---------------------------------------
    # Find customer
    # ---------------------------------------
    customer = customer_df[
        customer_df["customerID"].astype(str).str.strip()
        == str(customer_id).strip()
    ]

    if customer.empty:
        return {
            "all": [],
            "positive": [],
            "negative": []
        }

    # ---------------------------------------
    # Get one customer
    # ---------------------------------------
    customer_row = customer.iloc[0].copy()

    # ---------------------------------------
    # Prepare features
    # ---------------------------------------
    customer_features = prepare_customer_features(
        customer_row
    )

    # ---------------------------------------
    # Create DataFrame
    # ---------------------------------------
    X = pd.DataFrame([customer_features])

    X = X.drop(
        columns=["customerID", "Churn"],
        errors="ignore"
    )

    # ---------------------------------------
    # Transform using same preprocessor
    # ---------------------------------------
    X_processed = preprocessor.transform(X)

    # ---------------------------------------
    # Feature names
    # ---------------------------------------
    feature_names = preprocessor.get_feature_names_out()

    # ---------------------------------------
    # Create SHAP explainer
    # ---------------------------------------
    explainer = shap.TreeExplainer(
        xgboost_model
    )

    shap_values = explainer.shap_values(
        X_processed
    )

    # ---------------------------------------
    # Handle different SHAP output formats
    # ---------------------------------------

    if isinstance(shap_values, list):

        # Binary classification
        if len(shap_values) > 1:
            shap_values = shap_values[1]
        else:
            shap_values = shap_values[0]

    shap_values = np.asarray(shap_values)

    # Remove batch dimension
    if shap_values.ndim == 2:
        shap_values = shap_values[0]

    # Some SHAP versions can return
    # (samples, features, classes)
    elif shap_values.ndim == 3:
        shap_values = shap_values[0, :, 1]

    # ---------------------------------------
    # Make sure lengths match
    # ---------------------------------------

    feature_names = list(feature_names)

    if len(feature_names) != len(shap_values):

        print(
            "SHAP feature mismatch:",
            len(feature_names),
            len(shap_values)
        )

        return {
            "all": [],
            "positive": [],
            "negative": []
        }

    # ---------------------------------------
    # Build SHAP result
    # ---------------------------------------

    results = []

    for feature_name, value in zip(
        feature_names,
        shap_values
    ):

        value = float(value)

        results.append({
            "feature": str(feature_name),
            "shap_value": value,
            "impact": (
                "increases"
                if value > 0
                else "decreases"
            )
        })

    # ---------------------------------------
    # Sort by absolute impact
    # ---------------------------------------

    results.sort(
        key=lambda x: abs(x["shap_value"]),
        reverse=True
    )

    # ---------------------------------------
    # Top factors
    # ---------------------------------------

    top_results = results[:top_n]

    positive = [
        item
        for item in top_results
        if item["shap_value"] > 0
    ]

    negative = [
        item
        for item in top_results
        if item["shap_value"] < 0
    ]

    return {
        "all": top_results,
        "positive": positive,
        "negative": negative
    }


# ============================================================
# KNOWLEDGE BASE SEARCH
# ============================================================

def search_knowledge_base(query, top_k=3):
    """
    Search the local FAISS knowledge base and return
    the most relevant knowledge chunks.
    """

    # Create query embedding
    query_embedding = embedding_model.encode(
        [query],
        normalize_embeddings=True
    )

    query_embedding = np.asarray(
        query_embedding,
        dtype="float32"
    )

    # FAISS search
    scores, indices = knowledge_index.search(
        query_embedding,
        top_k
    )

    results = []

    for score, index in zip(scores[0], indices[0]):

        # Ignore invalid FAISS indices
        if index < 0:
            continue

        # IMPORTANT:
        # knowledge_metadata is a DataFrame,
        # so use .iloc[index] for row access.
        if isinstance(knowledge_metadata, pd.DataFrame):
            item = knowledge_metadata.iloc[int(index)]
            item = item.to_dict()

        # If metadata is a normal Python list
        else:
            item = knowledge_metadata[int(index)]

        results.append({
            "score": float(score),
            "content": item.get(
                "content",
                item.get(
                    "text",
                    item.get("chunk", "")
                )
            ),
            "source": item.get(
                "source",
                "Knowledge Base"
            )
        })

    return results
# ============================================================
# AI RESPONSE
# ============================================================

def generate_ai_response(
    question,
    customer_id=None
):
    load_local_llm()
    profile = None
    churn = None
    shap_result = None

    if customer_id:

        profile = get_customer_profile(
            customer_id
        )

        churn = predict_churn(
            customer_id
        )

        shap_result = get_shap_explanation(
            customer_id
        )

    knowledge = search_knowledge_base(
        question,
        top_k=3
    )

    verified_context = {
        "customer_profile": profile,
        "churn_prediction": churn,
        "shap_explanation": shap_result,
        "knowledge_base": knowledge
    }

    prompt = f"""
You are a customer intelligence assistant.

Answer the user's question using ONLY
the verified information below.

Do not invent customer information.

Do not invent churn probabilities.

Do not change numerical values.

Clearly distinguish:
1. Customer information
2. ML prediction
3. SHAP evidence
4. Business policy information

If information is unavailable, say so.

Keep the answer simple and useful.

USER QUESTION:
{question}

VERIFIED INFORMATION:
{json.dumps(
    verified_context,
    indent=2,
    default=str
)}

FINAL ANSWER:
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=2048
    )

    with torch.no_grad():

        outputs = llm_model.generate(
            **inputs,
            max_new_tokens=180,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id
        )

    generated_tokens = outputs[
        0
    ][
        inputs["input_ids"].shape[1]:
    ]

    answer = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True
    )

    return {
        "answer": answer.strip(),
        "profile": profile,
        "churn": churn,
        "shap": shap_result,
        "knowledge": knowledge
    }


# ============================================================
# DASHBOARD
# ============================================================

@app.route("/")
def dashboard():

    total_customers = len(
        customer_df
    )

    churned = (
        customer_df["Churn"]
        .astype(str)
        .str.lower()
        .eq("yes")
        .sum()
    )

    churn_rate = (
        churned / total_customers
    ) * 100

    avg_monthly = (
        customer_df["MonthlyCharges"]
        .mean()
    )

    high_risk_count = len(
        customer_df[
            customer_df["MonthlyCharges"]
            >= customer_df["MonthlyCharges"]
            .quantile(0.75)
        ]
    )

    contract_data = (
        customer_df[
            "Contract"
        ]
        .value_counts()
        .to_dict()
    )

    internet_data = (
        customer_df[
            "InternetService"
        ]
        .value_counts()
        .to_dict()
    )

    churn_data = (
        customer_df[
            "Churn"
        ]
        .value_counts()
        .to_dict()
    )

    return render_template(
        "dashboard.html",
        total_customers=total_customers,
        churned=churned,
        churn_rate=round(
            churn_rate,
            2
        ),
        avg_monthly=round(
            avg_monthly,
            2
        ),
        high_risk_count=high_risk_count,
        contract_data=contract_data,
        internet_data=internet_data,
        churn_data=churn_data
    )


# ============================================================
# CUSTOMER PROFILE
# ============================================================

@app.route(
    "/customer",
    methods=[
        "GET",
        "POST"
    ]
)
def customer():

    profile = None
    prediction = None

    customer_id = request.values.get(
        "customer_id",
        ""
    ).strip()

    if customer_id:

        profile = get_customer_profile(
            customer_id
        )

        prediction = predict_churn(
            customer_id
        )

    return render_template(
        "customer.html",
        profile=profile,
        prediction=prediction,
        customer_id=customer_id
    )


# ============================================================
# SHAP PAGE
# ============================================================

@app.route("/explain", methods=["GET", "POST"])
def explain():

    customer_id = None
    profile = None
    prediction = None
    shap_result = {
        "all": [],
        "positive": [],
        "negative": []
    }

    error = None
    shap_error = None

    if request.method == "POST":

        customer_id = request.form.get(
            "customer_id",
            ""
        ).strip()

        if not customer_id:

            error = "Please enter a Customer ID."

        else:

            try:

                # -----------------------------
                # Find customer
                # -----------------------------

                customer = customer_df[
                    customer_df["customerID"]
                    .astype(str)
                    .str.strip()
                    == str(customer_id).strip()
                ]

                if customer.empty:

                    error = (
                        f"Customer '{customer_id}' "
                        "was not found."
                    )

                else:

                    profile = customer.iloc[0].to_dict()

                    # -----------------------------
                    # Prediction
                    # -----------------------------

                    prediction = predict_churn(
                        customer_id
                    )

                    # -----------------------------
                    # SHAP
                    # -----------------------------

                    try:

                        shap_result = (
                            get_shap_explanation(
                                customer_id
                            )
                        )

                    except Exception as e:

                        import traceback

                        print(
                            "\nSHAP ERROR:"
                        )

                        traceback.print_exc()

                        shap_error = str(e)

            except Exception as e:

                import traceback

                print(
                    "\nPREDICTION ERROR:"
                )

                traceback.print_exc()

                error = f"Analysis error: {str(e)}"

    return render_template(
        "explain.html",
        customer_id=customer_id,
        profile=profile,
        prediction=prediction,
        shap=shap_result,
        error=error,
        shap_error=shap_error
    )

# ============================================================
# AI ASSISTANT
# ============================================================

@app.route(
    "/assistant",
    methods=[
        "GET",
        "POST"
    ]
)
def assistant():

    answer = None
    customer_id = ""
    question = ""

    if request.method == "POST":

        customer_id = request.form.get(
            "customer_id",
            ""
        ).strip()

        question = request.form.get(
            "question",
            ""
        ).strip()

        if question:

            result = generate_ai_response(
                question,
                customer_id
                if customer_id
                else None
            )

            answer = result["answer"]

    return render_template(
        "assistant.html",
        answer=answer,
        customer_id=customer_id,
        question=question
    )


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )