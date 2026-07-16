# Phase 1 – Data Understanding

## 1. Objective

The purpose of this phase was to understand the hotel booking dataset before performing any preprocessing or analysis. This phase helped in identifying the dataset structure, missing values, duplicate records, data types, and overall quality of the data.

---

# 2. Dataset Overview

The Hotel Booking Demand dataset contains booking information collected from two different hotel types: City Hotel and Resort Hotel.

The dataset consists of customer details, booking information, hotel information, stay duration, pricing details, reservation status, and market information.

The dataset is suitable for performing data analysis, visualization, statistical analysis, and machine learning tasks.

---

# 3. Dataset Information

| Property | Value |
|-----------|-------|
| Dataset Name | Hotel Booking Demand Dataset |
| Source | Kaggle |
| Total Records | 119,390 |
| Total Columns | 32 |
| Numerical Columns | XX |
| Categorical Columns | XX |

---

# 4. Libraries Used

The following Python libraries were imported during this phase.

- Pandas
- NumPy
- Matplotlib
- Seaborn

These libraries were used to load the dataset, inspect the data, and perform basic exploratory analysis.

---

# 5. Dataset Loading

The dataset was loaded using the Pandas library.

The first five records were displayed to verify whether the dataset was loaded correctly.

### Output

```
df.head()
```

Observation

- Dataset loaded successfully.
- Column names are readable.
- Data appears consistent.

---

# 6. Dataset Shape

The dataset shape was checked to determine the total number of observations and features.

### Output

```
Rows : 119390

Columns : 32
```

Observation

The dataset contains sufficient records for performing statistical analysis and visualization.

---

# 7. Column Information

The dataset contains customer details, booking information, pricing information, and hotel details.

Important columns include:

| Column | Description |
|---------|-------------|
| hotel | Hotel Type |
| lead_time | Number of days before arrival the booking was made |
| adr | Average Daily Rate |
| adults | Number of adults |
| children | Number of children |
| babies | Number of babies |
| country | Customer Country |
| market_segment | Booking Source |
| customer_type | Customer Category |
| reservation_status | Booking Status |

---

# 8. Data Types

The data types of every feature were inspected.

| Data Type | Count |
|-----------|------:|
| Integer | XX |
| Float | XX |
| Object | XX |

Observation

- Numerical columns can be used for statistical analysis.
- Categorical columns will be useful for grouping and visualization.

---

# 9. Missing Value Analysis

Missing values were identified using the `isnull()` function.

| Column | Missing Values |
|---------|---------------:|
| company | 112593 |
| agent | 16340 |
| country | 488 |
| children | 4 |

### Observation

- Company contains the highest number of missing values.
- Agent also contains many missing values.
- Children contains only four missing records.
- Country contains a very small number of missing values.

These missing values will be handled during preprocessing.

---

# 10. Duplicate Record Analysis

Duplicate records were identified using the duplicated() function.

| Description | Count |
|-------------|------:|
| Duplicate Records | 31994 |

Observation

A large number of duplicate records are available in the dataset.

These records may affect statistical analysis and therefore will be removed during preprocessing.

---

# 11. Statistical Summary

Descriptive statistics were generated for all numerical columns.

| Feature | Mean | Minimum | Maximum |
|----------|-----:|--------:|--------:|
| Lead Time | 104.01 | 0 | 737 |
| ADR | 101.83 | -6.38 | 5400 |
| Adults | 1.86 | 0 | 55 |
| Children | 0.10 | 0 | 10 |
| Babies | 0.01 | 0 | 10 |

### Observation

- ADR contains extreme values.
- Lead Time varies significantly.
- Most bookings contain one or two adults.
- Babies are present only in a small number of bookings.

---

# 12. Distribution of Features

The numerical and categorical columns were reviewed to understand their distribution.

Key findings include:

- Majority of bookings belong to City Hotel.
- Portugal has the highest number of bookings.
- Most customers are classified as Transient.
- Online Travel Agencies contribute the highest bookings.

---

# 13. Initial Business Understanding

Based on the initial exploration, the following observations were made.

- City Hotel appears to receive more bookings.
- Customer behaviour differs across hotel types.
- Lead Time varies significantly among bookings.
- ADR contains possible outliers.
- Missing values require preprocessing before analysis.

---

# 14. Outputs Generated

The following outputs were generated during this phase.

- Dataset Preview
- Dataset Shape
- Dataset Information
- Column Details
- Missing Value Report
- Duplicate Record Report
- Statistical Summary
- Initial Observations

---

# 15. Conclusion

The Data Understanding phase successfully explored the structure and quality of the dataset. Missing values, duplicate records, and outliers were identified. The dataset was confirmed to be suitable for further preprocessing and statistical analysis.

The findings from this phase were used as the foundation for the Data Preprocessing phase.
