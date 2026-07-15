import plotly.express as px
import plotly.graph_objects as go
from .data_loader import load_data
from .analytics import (
    monthly_revenue,
    revenue_by_category,
    revenue_by_state,
    payment_distribution,
    review_distribution,
    top_products,
    top_sellers,
    customer_spending,
    delivery_performance
)

customer = (
    load_data()
    .groupby("customer_unique_id")["payment_value"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

# COMMON LAYOUT


def apply_layout(fig):

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#162B46",
        plot_bgcolor="#162B46",
        font=dict(
            family="Poppins",
            color="white"
        ),
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),
        height=420
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="#2b3d56",
        zeroline=False
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="#2b3d56",
        zeroline=False
    )

    return fig


# MONTHLY SALES


def monthly_sales_chart():

    data = monthly_revenue()

    fig = px.line(

        data,

        x="purchase_month",

        y="payment_value",

        markers=True,

        title="Monthly Revenue Trend"

    )

    fig.update_traces(

        line=dict(width=4),

        marker=dict(size=10)

    )

    return apply_layout(fig).to_html(full_html=False)



# CATEGORY REVENUE


def category_chart():

    data = revenue_by_category()

    fig = px.bar(

        data,

        x="payment_value",

        y="product_category_name_english",

        orientation="h",

        color="payment_value",

        title="Top Categories"

    )

    fig.update_layout(yaxis=dict(categoryorder="total ascending"))

    return apply_layout(fig).to_html(full_html=False)



# STATE REVENUE


def state_chart():

    data = revenue_by_state()

    fig = px.bar(

        data,

        x="customer_state",

        y="payment_value",

        color="payment_value",

        title="Revenue by State"

    )

    return apply_layout(fig).to_html(full_html=False)



# PAYMENT METHODS


def payment_chart():

    data = payment_distribution()

    fig = px.pie(

        data,

        names="payment_type",

        values="count",

        hole=0.55,

        title="Payment Methods"

    )

    fig.update_traces(textposition="inside")

    return apply_layout(fig).to_html(full_html=False)



# REVIEW SCORE


def review_chart():

    data = review_distribution()

    fig = px.bar(

        data,

        x="review_score",

        y="count",

        color="count",

        title="Review Score Distribution"

    )

    return apply_layout(fig).to_html(full_html=False)





# CUSTOMER SPENDING


def customer_chart():

    data = customer_spending()

    fig = px.bar(

        data,

        x="customer_unique_id",

        y="payment_value",

        color="payment_value",

        title="Top Customer Spending"

    )

    fig.update_xaxes(showticklabels=False)

    return apply_layout(fig).to_html(full_html=False)



# TOP SELLERS


def seller_chart():

    data = top_sellers()

    fig = px.bar(

        data,

        x="seller_id",

        y="Revenue",

        color="Revenue",

        title="Top Sellers"

    )

    fig.update_xaxes(showticklabels=False)

    return apply_layout(fig).to_html(full_html=False)



# PRODUCT REVENUE


def product_chart():

    data = top_products()

    fig = px.bar(
        data,
        x="Revenue",
        y="product_category_name_english",
        orientation="h",
        color="Revenue",
        title="Best Selling Categories"
    )

    fig.update_layout(

        yaxis=dict(categoryorder="total ascending")

    )

    return apply_layout(fig).to_html(full_html=False)



# DELIVERY PERFORMANCE


def delivery_chart():

    data = delivery_performance()

    fig = px.bar(

        data,

        x="customer_state",

        y="delivery_time_days",

        color="delivery_time_days",

        title="Average Delivery Time"

    )

    return apply_layout(fig).to_html(full_html=False)



# DELIVERY SCATTER


def delivery_scatter():

    data = delivery_performance()

    fig = px.scatter(

        data,

        x="customer_state",

        y="delivery_time_days",

        size="delivery_time_days",

        color="delivery_time_days",

        title="Delivery Performance"

    )

    return apply_layout(fig).to_html(full_html=False)



# SALES HEATMAP


def sales_heatmap():

    data = monthly_revenue()

    fig = go.Figure(

        data=go.Heatmap(

            z=[data["payment_value"]],

            x=data["purchase_month"],

            colorscale="Viridis"

        )

    )

    fig.update_layout(

        title="Monthly Sales Heatmap"

    )

    return apply_layout(fig).to_html(full_html=False)



# REVENUE AREA CHART


def revenue_area_chart():

    data = monthly_revenue()

    fig = px.area(

        data,

        x="purchase_month",

        y="payment_value",

        title="Revenue Area Trend"

    )

    return apply_layout(fig).to_html(full_html=False)



# CATEGORY TREEMAP


def category_treemap():

    data = revenue_by_category()

    fig = px.treemap(

        data,

        path=["product_category_name_english"],

        values="payment_value",

        title="Revenue Treemap"

    )

    return apply_layout(fig).to_html(full_html=False)



# SELLER PIE

#Revenue_chart
def seller_revenue_chart():

    df = load_data()

    revenue = (
        df.groupby("seller_id")["payment_value"]
        .sum()
        .sort_values(ascending=False)
        .head(20)
        .reset_index()
    )

    fig = px.histogram(
        revenue,
        x="payment_value",
        nbins=20,
        color="payment_value",
        title="Seller Revenue Distribution"
    )

    return apply_layout(fig).to_html(full_html=False)
def seller_chart():

    data = top_sellers()

    fig = px.bar(

        data,

        x="seller_id",

        y="Revenue",

        color="Revenue",

        title="Top Sellers"

    )

    fig.update_xaxes(showticklabels=False)

    return apply_layout(fig).to_html(full_html=False)


#seller_delivery-chart
def seller_delivery_chart():

    df = load_data()

    delivery = (
        df.groupby("seller_state")["delivery_time_days"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        delivery,
        x="seller_state",
        y="delivery_time_days",
        color="delivery_time_days",
        title="Average Delivery Time"
    )

    return apply_layout(fig).to_html(full_html=False)
def seller_pie_chart():

    data = top_sellers()

    fig = px.pie(

        data,

        names="seller_id",

        values="Revenue",

        hole=0.45,

        title="Top Seller Contribution"

    )

    return apply_layout(fig).to_html(full_html=False)
#seller_state_chart
def seller_state_chart():

    df = load_data()

    state = (
        df.groupby("seller_state")
        .size()
        .reset_index(name="Total Sellers")
        .sort_values("Total Sellers", ascending=False)
    )

    fig = px.pie(
        state,
        names="seller_state",
        values="Total Sellers",
        hole=0.55,
        title="Seller Distribution"
    )

    fig.update_traces(textinfo="percent")

    fig.update_layout(
        height=420,
        showlegend=False,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    return apply_layout(fig).to_html(full_html=False)


# REVIEW DONUT


def review_donut():

    data = review_distribution()

    fig = px.pie(

        data,

        names="review_score",

        values="count",

        hole=0.60,

        title="Review Distribution"

    )

    return apply_layout(fig).to_html(full_html=False)
def customer_state_chart():

    df = load_data()

    state = (
        df.groupby("customer_state")
        .size()
        .reset_index(name="Customers")
        .sort_values("Customers", ascending=False)
    )

    fig = px.bar(
        state,
        x="customer_state",
        y="Customers",
        color="Customers",
        title="Customers by State",
        template="plotly_dark"
    )

    fig.update_layout(
        paper_bgcolor="#162B46",
        plot_bgcolor="#162B46",
        font=dict(color="white"),
        coloraxis_showscale=False,
        height=420
    )

    return apply_layout(fig).to_html(full_html=False)
def customer_spending_chart():

    df = load_data()

    customer = (
        df.groupby("customer_unique_id")["payment_value"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        customer,
        x="customer_unique_id",
        y="payment_value",
        color="payment_value",
        title="Top 10 Customers by Spending",
        template="plotly_dark"
    )

    fig.update_xaxes(showticklabels=False)

    fig.update_layout(
        paper_bgcolor="#162B46",
        plot_bgcolor="#162B46",
        font=dict(color="white"),
        coloraxis_showscale=False,
        height=420
    )

    return apply_layout(fig).to_html(full_html=False)
def repeat_customer_chart():

    df = load_data()

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

    fig = px.bar(
        repeat,
        x="Purchase Count",
        y="Number of Customers",
        color="Number of Customers",
        title="Repeat Customer Analysis",
        template="plotly_dark"
    )

    fig.update_layout(
        paper_bgcolor="#162B46",
        plot_bgcolor="#162B46",
        font=dict(color="white"),
        coloraxis_showscale=False,
        height=420
    )

    return apply_layout(fig).to_html(full_html=False)
import plotly.graph_objects as go

def review_gauge_chart():

    df = load_data()

    avg = round(df["review_score"].mean(), 2)

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=avg,
        number={"suffix": " / 5"},
        title={"text": "Average Review Score"},
        gauge={
            "axis": {"range": [0, 5]},
            "bar": {"color": "#6C63FF"},
            "steps": [
                {"range": [0, 2], "color": "#ff4d4d"},
                {"range": [2, 3.5], "color": "#ffa500"},
                {"range": [3.5, 5], "color": "#00c896"}
            ]
        }
    ))

    return apply_layout(fig).to_html(full_html=False)