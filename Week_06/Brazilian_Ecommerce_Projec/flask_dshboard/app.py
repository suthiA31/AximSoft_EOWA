from flask import Flask, render_template
from utils.analytics import seller_kpis


# Import Analytics


from utils.analytics import (
    dashboard_kpis,
    recent_orders,
    full_dataset,
    top_sellers
)
from utils.charts import *

# Import Charts


from utils.charts import (
    monthly_sales_chart,
    category_chart,
    state_chart,
    payment_chart,
    review_chart,
    customer_chart,
    seller_chart,
    product_chart,
    delivery_chart,
    delivery_scatter,
    sales_heatmap,
    revenue_area_chart,
    category_treemap,
    seller_pie_chart,
    review_donut,
    seller_state_chart,
    seller_delivery_chart,
    seller_revenue_chart
)


# Flask App


app = Flask(__name__)


# DASHBOARD


@app.route("/")
def dashboard():

    kpis = dashboard_kpis()
    print(kpis)

    return render_template(

        "dashboard.html",

        kpis=kpis,

        monthly_chart=monthly_sales_chart(),

        payment_chart=payment_chart(),

        category_chart=category_chart(),

        state_chart=state_chart(),

        rreview_chart=review_gauge_chart(),

        recent_orders=recent_orders().to_dict(orient="records"),

        top_products=top_products().to_dict(orient="records"),
        top_sellers = top_sellers().to_dict(orient="records")
    )


# SALES


@app.route("/sales")
def sales():

    kpis = dashboard_kpis()

    return render_template(

        "sales.html",

        kpis=kpis,

        monthly_chart=monthly_sales_chart(),

        revenue_area=revenue_area_chart(),

        category_chart=category_chart(),

        state_chart=state_chart(),

        heatmap=sales_heatmap()

    )


# CUSTOMERS


@app.route("/customers")
def customers():

    return render_template(

        "customers.html",

        kpis=dashboard_kpis(),

        customer_chart=customer_spending_chart(),

        review_chart=review_chart(),

        customer_state_chart=customer_state_chart(),

        repeat_customer_chart=repeat_customer_chart()

    )


# PRODUCTS


@app.route("/products")
def products():

    return render_template(

        "products.html",

        kpis=dashboard_kpis(),

        product_chart=product_chart(),

        treemap=category_treemap()

    )


# SELLERS


@app.route("/sellers")
def sellers():
    print("seller_state_chart:", len(seller_state_chart()))

    return render_template(
        "sellers.html",
        kpis=seller_kpis(),
        seller_chart=seller_chart(),
        seller_state_chart=seller_state_chart(),
        delivery_chart=seller_delivery_chart(),
        seller_revenue_chart=seller_revenue_chart(),
        top_sellers=top_sellers().to_dict("records")
    )


# DELIVERY


@app.route("/delivery")
def delivery():

    return render_template(

        "delivery.html",

        kpis=dashboard_kpis(),

        delivery_chart=delivery_chart(),

        scatter=delivery_scatter()

    )


# PAYMENTS & REVIEWS


@app.route("/payments")
def payments():

    return render_template(

        "payments.html",

        kpis=dashboard_kpis(),

        payment_chart=payment_chart(),

        review_chart=review_chart(),

        review_donut=review_donut()

    )


# DATASET EXPLORER


@app.route("/explorer")
def explorer():

    data = full_dataset()

    return render_template(

        "explorer.html",

        tables=data.head(1000).to_dict(orient="records"),

        columns=data.columns

    )
@app.route("/login")
def login():

    return render_template("login.html")


# ERROR PAGE


@app.errorhandler(404)
def page_not_found(error):

    return render_template("404.html"),404


# RUN


if __name__ == "__main__":

    app.run(

        debug=True,

        host="127.0.0.1",

        port=5000

    )