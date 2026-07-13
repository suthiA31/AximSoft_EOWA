import pandas as pd
from .data_loader import load_data


# Load Dataset


df = load_data()


# Dashboard KPIs


def dashboard_kpis():

    
    # Basic KPIs
    

    total_revenue = df["payment_value"].sum()

    total_orders = df["order_id"].nunique()

    total_customers = df["customer_unique_id"].nunique()

    total_sellers = df["seller_id"].nunique()

    
    # Average Order Value
    

    average_order_value = (

        df.groupby("order_id")["payment_value"]

        .sum()

        .mean()

    )

    
    # Average Review
    

    average_review_score = df["review_score"].mean()

    
    # Average Delivery Time
    

    average_delivery_time = df["delivery_time_days"].mean()

    
    # Revenue Growth
    

    monthly_sales = (

        df.groupby("purchase_month")["payment_value"]

        .sum()

        .sort_index()

    )

    if len(monthly_sales) >= 2:

        current_month = monthly_sales.iloc[-1]

        previous_month = monthly_sales.iloc[-2]

        if previous_month != 0:

            revenue_growth = (

                (current_month - previous_month)

                / previous_month

            ) * 100

        else:

            revenue_growth = 0

    else:

        revenue_growth = 0

    
    # Repeat Customers
    

    customer_orders = (

        df.groupby("customer_unique_id")

        .size()

    )

    repeat_customers = (

        customer_orders > 1

    ).sum()

    repeat_customer_rate = (

        repeat_customers / total_customers

    ) * 100

    
    # Top State
    

    top_state = (

        df.groupby("customer_state")["payment_value"]

        .sum()

        .idxmax()

    )

    
    # Top Category
    

    top_category = (

        df.groupby("product_category_name_english")["payment_value"]

        .sum()

        .idxmax()

    )

    
    # Top Payment Method
    

    top_payment_method = (

        df["payment_type"]

        .value_counts()

        .idxmax()

    )

    
    # Delayed Orders
    

    delayed_orders = (

        df["delivery_time_days"]

        > df["delivery_time_days"].median()

    ).sum()

    delayed_percentage = (

        delayed_orders / len(df)

    ) * 100

    
    # Seller KPIs
    

    seller_revenue = (

        df.groupby("seller_id")["payment_value"]

        .sum()

    )

    top_seller_revenue = seller_revenue.max()

    avg_seller_revenue = seller_revenue.mean()

    
    # Product KPIs
    

    avg_product_price = df["price"].mean()

    top_product_revenue = (

        df.groupby("product_category_name_english")["payment_value"]

        .sum()

        .max()

    )

    
    # Return Dictionary
    

    return {

        "revenue": round(total_revenue, 2),

        "orders": total_orders,

        "customers": total_customers,

        "sellers": total_sellers,

        "avg_order": round(average_order_value, 2),

        "avg_review": round(average_review_score, 2),

        "avg_delivery": round(average_delivery_time, 2),

        "growth": round(revenue_growth, 2),

        "repeat_rate": round(repeat_customer_rate, 2),

        "top_state": top_state,

        "top_category": top_category,

        "top_payment": top_payment_method,

        "delayed_rate": round(delayed_percentage, 2),

        "top_seller_revenue": round(top_seller_revenue, 2),

        "avg_seller_revenue": round(avg_seller_revenue, 2),

        "avg_product_price": round(avg_product_price, 2),

        "top_product_revenue": round(top_product_revenue, 2)

    }

# Monthly Revenue


def monthly_revenue():

    return (

        df.groupby("purchase_month")["payment_value"]

        .sum()

        .reset_index()

    )


# Revenue by Category


def revenue_by_category():

    return (

        df.groupby("product_category_name_english")["payment_value"]

        .sum()

        .sort_values(ascending=False)

        .head(10)

        .reset_index()

    )


# Revenue by State


def revenue_by_state():

    return (

        df.groupby("customer_state")["payment_value"]

        .sum()

        .sort_values(ascending=False)

        .head(10)

        .reset_index()

    )


# Payment Distribution


def payment_distribution():

    return (

        df.groupby("payment_type")

        .size()

        .reset_index(name="count")

    )


# Review Distribution


def review_distribution():

    return (

        df.groupby("review_score")

        .size()

        .reset_index(name="count")

    )


# Top Products


def top_products():

    products = (

        df.groupby("product_category_name_english")

        .agg(

            Revenue=("payment_value","sum"),

            Orders=("order_id","nunique"),

            Average_Review=("review_score","mean")

        )

        .sort_values("Revenue",ascending=False)

        .head(10)

        .reset_index()

    )

    products["Average_Review"] = products["Average_Review"].round(2)

    products["Revenue"] = products["Revenue"].round(2)

    return products


# Top Sellers


def top_sellers():

    sellers = (

        df.groupby("seller_id")

        .agg(

            Revenue=("payment_value", "sum"),

            Orders=("order_id", "nunique"),

            Avg_Review=("review_score", "mean"),

            Avg_Delivery=("delivery_time_days", "mean")

        )

        .sort_values("Revenue", ascending=False)

        .head(10)

        .reset_index()

    )

    sellers["Revenue"] = sellers["Revenue"].round(2)
    sellers["Avg_Review"] = sellers["Avg_Review"].round(2)
    sellers["Avg_Delivery"] = sellers["Avg_Delivery"].round(1)

    return sellers


# Customer Spending


def customer_spending():

    return (

        df.groupby("customer_unique_id")["payment_value"]

        .sum()

        .sort_values(ascending=False)

        .head(10)

        .reset_index()

    )


# Delivery Performance


def delivery_performance():

    return (

        df.groupby("customer_state")["delivery_time_days"]

        .mean()

        .sort_values()

        .reset_index()

    )


# Recent Orders


def recent_orders():

    recent = (

        df[[
            "order_id",
            "customer_city",
            "customer_state",
            "payment_value",
            "review_score",
            "delivery_time_days"
        ]]

        .sort_values(
            by="payment_value",
            ascending=False
        )

        .head(15)

        .copy()

    )

    recent["Status"] = recent["delivery_time_days"].apply(

        lambda x: "On Time" if x <= df["delivery_time_days"].median()
        else "Delayed"

    )

    return recent


# Entire Dataset


def full_dataset():

    return df
# ==========================================================
# SELLER KPIs
# ==========================================================

def seller_state_distribution():

    return (

        df.groupby("seller_state")

        .size()

        .reset_index(name="Total Sellers")

        .sort_values("Total Sellers", ascending=False)

    )


def seller_revenue():

    return (

        df.groupby("seller_id")["payment_value"]

        .sum()

        .reset_index(name="Revenue")

        .sort_values("Revenue", ascending=False)

        .head(10)

    )


def seller_revenue_distribution():

    return (

        df.groupby("seller_id")["payment_value"]

        .sum()

        .reset_index(name="Revenue")

    )


def top_sellers_table():

    table = (

        df.groupby("seller_id")

        .agg(

            payment_value=("payment_value", "sum"),

            total_orders=("order_id", "nunique"),

            average_review=("review_score", "mean"),

            average_delivery=("delivery_time_days", "mean")

        )

        .sort_values("payment_value", ascending=False)

        .head(20)

        .reset_index()

    )

    table["average_review"] = table["average_review"].round(2)

    table["average_delivery"] = table["average_delivery"].round(1)

    return table.to_dict("records")


# ==========================================================
# CUSTOMER
# ==========================================================

def customer_state_distribution():

    return (

        df.groupby("customer_state")

        .size()

        .reset_index(name="Customers")

        .sort_values("Customers", ascending=False)

    )


def repeat_customer_distribution():

    repeat = (

        df.groupby("customer_unique_id")

        .size()

        .value_counts()

        .sort_index()

        .reset_index()

    )

    repeat.columns = [

        "Purchase Count",

        "Number of Customers"

    ]

    return repeat


# ==========================================================
# PRODUCT
# ==========================================================

def product_price_distribution():

    return df[["price"]]


def product_popularity():

    return (

        df.groupby("product_category_name_english")

        .size()

        .reset_index(name="Orders")

        .sort_values("Orders", ascending=False)

        .head(10)

    )


# ==========================================================
# PAYMENT
# ==========================================================

def installment_distribution():

    return (

        df.groupby("payment_installments")

        .size()

        .reset_index(name="Count")

    )


# ==========================================================
# DELIVERY
# ==========================================================

def delayed_orders():

    return (

        df.groupby("delayed")

        .size()

        .reset_index(name="Orders")

    )


# ==========================================================
# DATA EXPLORER
# ==========================================================

def dataset_preview():

    return df.head(100).to_dict("records")


# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

def executive_summary():

    return {

        "Total Revenue": round(df["payment_value"].sum(),2),

        "Total Orders": df["order_id"].nunique(),

        "Total Customers": df["customer_unique_id"].nunique(),

        "Total Sellers": df["seller_id"].nunique(),

        "Average Review": round(df["review_score"].mean(),2),

        "Average Delivery": round(df["delivery_time_days"].mean(),2),

        "Average Order Value": round(df.groupby("order_id")["payment_value"].sum().mean(),2)

    }
def seller_kpis():

    df = load_data()

    seller_summary = (
        df.groupby("seller_id")
        .agg(
            Revenue=("payment_value", "sum"),
            Delivery=("delivery_time_days", "mean")
        )
    )

    return {

        "sellers": df["seller_id"].nunique(),

        "top_seller_revenue": seller_summary["Revenue"].max(),

        "avg_seller_revenue": seller_summary["Revenue"].mean(),

        "avg_delivery": round(
            seller_summary["Delivery"].mean(), 2
        )

    }