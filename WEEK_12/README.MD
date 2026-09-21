# AI Customer Intelligence Platform

## 1. Project Overview

The **AI Customer Intelligence Platform** is a lightweight, locally deployable customer analytics and AI system that combines traditional data analytics, SQL, machine learning, explainable AI, customer-support text analysis, semantic search, Retrieval-Augmented Generation (RAG), and a small local Large Language Model (LLM).

The platform is designed to provide customer intelligence without relying on paid cloud AI services, external APIs, or dedicated GPU infrastructure.

The system uses:

* Customer churn analytics
* SQL-based customer analysis
* Feature engineering
* Machine learning
* Ensemble learning
* Model improvement and threshold tuning
* SHAP explainability
* Customer-support NLP
* TF-IDF classification
* Sentence embeddings
* FAISS semantic search
* Knowledge-base retrieval
* RAG
* A local small instruction-tuned LLM
* Prompt engineering
* Tool calling
* A simple AI agent workflow
* GenAI evaluation
* Resource benchmarking
* Flask web application

The main goal is to demonstrate how a resource-efficient AI system can combine structured customer intelligence with unstructured business knowledge and explainable machine learning.

---

# 2. Research Question

> **Can a lightweight, locally deployable AI system combine traditional customer analytics, machine learning, explainable AI, semantic retrieval, and a small local LLM to provide reliable and resource-efficient customer intelligence without relying on paid cloud AI services?**

---

# 3. Objectives

The project has the following objectives:

1. Perform exploratory analysis of customer data.
2. Use SQL for structured customer analytics.
3. Build a reliable preprocessing pipeline.
4. Engineer customer-level behavioral and risk features.
5. Develop baseline churn prediction models.
6. Compare ensemble machine-learning models.
7. Improve the selected model using class weighting, cross-validation, hyperparameter tuning, and threshold adjustment.
8. Explain model predictions using SHAP.
9. Analyze customer-support text using NLP.
10. Build a TF-IDF-based ticket classification system.
11. Generate sentence embeddings for semantic retrieval.
12. Implement local FAISS vector search.
13. Build a business knowledge base.
14. Implement Retrieval-Augmented Generation.
15. Run a small local instruction-tuned LLM.
16. Compare different prompt-engineering approaches.
17. Integrate SQL, ML, SHAP, RAG, and LLM components.
18. Implement simple tool calling.
19. Build a simple customer-intelligence agent.
20. Evaluate GenAI responses.
21. Benchmark system resource usage and inference time.
22. Develop a lightweight Flask web application.

---

# 4. System Architecture

```text
                    ┌──────────────────────────┐
                    │     Customer Dataset     │
                    │    IBM Telco Churn       │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │
```
