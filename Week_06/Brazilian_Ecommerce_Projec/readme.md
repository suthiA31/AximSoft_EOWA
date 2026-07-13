# 🛒 Brazilian E-Commerce (Olist) Data Engineering & Analytics Project
 
## 📌 Project Overview
 
This project is an end-to-end Data Engineering and Analytics solution built using the Brazilian E-Commerce Public Dataset (Olist). The objective is to clean, preprocess, merge, analyze, and visualize the data to generate meaningful business insights.
 
The project follows a structured analytics workflow consisting of data understanding, preprocessing, feature engineering, exploratory data analysis (EDA), and an interactive dashboard developed using Flask and Bootstrap.
 
---
 
## 🎯 Project Objectives
 
- Load and understand multiple relational datasets.
- Perform data cleaning and preprocessing on each dataset individually.
- Merge datasets using appropriate keys.
- Engineer meaningful business features.
- Perform comprehensive Exploratory Data Analysis (EDA).
- Generate a Data Quality Report.
- Develop an interactive analytics dashboard using Flask and Bootstrap.
 
---
 
## 📂 Dataset
 
**Dataset Name:** Brazilian E-Commerce Public Dataset (Olist)
 
The project uses the following datasets:
 
- Customers
- Orders
- Order Items
- Products
- Sellers
- Payments
- Reviews
- Geolocation
- Product Category Translation
 
---
 
# 📁 Project Structure
 
```
Brazilian_Ecommerce_Project/
│
├── data/
│   ├── raw/
│   ├── processed/
│   │      clean_dataset.csv
│   │      feature_engineered_dataset.csv
│   │
│   └── reports/
│          data_quality_report.csv
│
├── notebook/
│      Olist_Data_Engineering.ipynb
│
├── flask_dashboard/
│      app.py
│      templates/
│      static/
│
├── images/
│
├── requirements.txt
│
└── README.md
```
 
---
 
# 🛠 Technologies Used
 
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Missingno
- Jupyter Notebook
- Flask
- Bootstrap 5
- HTML5
- CSS3
 
---
 
# 🚀 Project Workflow
 
```
Phase 1
│
├── Data Understanding
│
Phase 2
│
├── Data Cleaning
│
Phase 3
│
├── Feature Engineering
│
Phase 4
│
├── Exploratory Data Analysis
│
Phase 5
│
├── Data Quality Report
│
Flask Dashboard
```
 
---
 
# 📊 Phase 1 – Data Understanding
 
Completed Tasks
 
- Loaded all datasets
- Inspected dataset dimensions
- Examined data types
- Generated descriptive statistics
- Analyzed missing values
- Checked duplicate records
- Understood table relationships
- Planned dataset merge strategy
 
---
 
# 🧹 Phase 2 – Data Cleaning
 
Performed preprocessing on every dataset before merging.
 
Cleaning Tasks
 
- Missing value analysis
- Missing value treatment
- Duplicate removal
- Data type conversion
- Invalid data validation
- Outlier detection
- Outlier treatment
- Data validation
 
---
 
# ⚙ Phase 3 – Feature Engineering
 
Created business-oriented features including:
 
- Delivery Time
- Shipping Duration
- Processing Time
- Total Order Value
- Average Product Price
- Customer Purchase Count
- Customer Lifetime Value
- Revenue per Customer
- Seller Performance Score
- Average Review Score
- Monthly Sales
- Repeat Customer Indicator
 
---
 
# 📈 Phase 4 – Exploratory Data Analysis
 
Business analyses performed:
 
## Sales Analysis
 
- Monthly Sales Trend
- Revenue by Category
- Revenue by State
- Average Order Value
 
## Customer Analysis
 
- Customer Distribution
- Customer Spending
- Customer Lifetime Value
- Repeat Customers
- Top Purchasing Cities
 
## Product Analysis
 
- Best Selling Products
- Product Pricing
- Category Performance
- Product Popularity
 
## Seller Analysis
 
- Top Sellers
- Seller Revenue
- Seller Performance
 
## Delivery Analysis
 
- Delivery Time
- Delayed Deliveries
- Shipping Performance
 
## Payment Analysis
 
- Payment Methods
- Installment Analysis
- Payment Value Distribution
 
## Review Analysis
 
- Review Score Distribution
- Positive vs Negative Reviews
- Customer Satisfaction Trends
 
---
 
# 📋 Phase 5 – Data Quality Report
 
Generated reports including:
 
- Total records processed
- Missing values handled
- Duplicate records removed
- Outliers treated
- Features engineered
- Tables merged
- Final dataset dimensions
 
Exported files:
 
- Clean Dataset (.csv)
- Feature Engineered Dataset (.csv)
- Data Quality Report (.csv)
 
---
 
# 🌐 Flask Analytics Dashboard
 
The dashboard contains the following pages:
 
- Dashboard
- Sales Analytics
- Customer Analytics
- Product Analytics
- Seller Analytics
- Delivery Analytics
- Payment & Review Analytics
- Dataset Explorer
 
Dashboard Features
 
- KPI Cards
- Interactive Charts
- Search & Filter
- Sortable Tables
- Paginated Dataset Viewer
 
---
 
# 📊 Key Business Features Created
 
| Feature | Description |
|----------|-------------|
| Delivery Time | Time taken to deliver an order |
| Shipping Duration | Carrier to customer delivery duration |
| Processing Time | Purchase to shipment time |
| Total Order Value | Product price + freight cost |
| Customer Lifetime Value | Total customer spending |
| Seller Performance Score | Seller revenue and review-based score |
| Repeat Customer | Indicates multiple purchases |
| Monthly Sales | Monthly revenue trends |
 
---
 
# 📁 Output Files
 
After execution, the following files are generated:
 
```
processed/
 
clean_dataset.csv
 
feature_engineered_dataset.csv
 
reports/
 
data_quality_report.csv
```
 
---
 
# ▶ How to Run the Project
 
### 1. Clone the Repository
 
```bash
git clone <repository-url>
```
 
### 2. Install Dependencies
 
```bash
pip install -r requirements.txt
```
 
### 3. Run the Notebook
 
Open:
 
```
notebook/Olist_Data_Engineering.ipynb
```
 
Execute all cells sequentially.
 
### 4. Start Flask Dashboard
 
```bash
cd flask_dashboard
 
python app.py
```
 
Open your browser and visit:
 
```
http://127.0.0.1:5000
```
 
---
 
# 📌 Project Outcomes
 
This project demonstrates:
 
- Data Engineering
- Data Cleaning
- Relational Data Integration
- Feature Engineering
- Business Intelligence
- Exploratory Data Analysis
- Dashboard Development
- Data Visualization
 
---
 
# 👨‍💻 Author
 
**Name:** *Your Name*
 
**Course:** Data Engineering & Analytics Project
 
**Dataset:** Brazilian E-Commerce Public Dataset (Olist)
 
---
 
# 📜 License
 
This project is developed for educational purposes using the publicly available Olist dataset.
 
