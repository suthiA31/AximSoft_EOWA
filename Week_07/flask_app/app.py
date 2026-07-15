from flask import Flask


from analytics import *
from flask import request
from flask import jsonify, render_template
from charts.dashboard_charts import *


from insights import *
from charts.revenue_charts import *
from charts.statistics_charts import *
from charts.booking_charts import *
from charts.customer_charts import *
from filters import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("landing.html")

@app.route("/dashboard")

def dashboard():

    data = load_dataset()

    data = apply_filters(data, request)

    filters = filter_values(load_dataset())

    return render_template(

        "dashboard.html",

        hotels=filters["hotels"],

        countries=filters["countries"],

        segments=filters["segments"],

        customer_types=filters["customers"],

        years=filters["years"],

        seasons=filters["seasons"],

        kpi=get_dashboard_kpis(data),

        table=data.head(20),

        booking_chart=booking_trend(data),

        revenue_chart=revenue_trend(data),

        hotel_chart=hotel_distribution(data),

        cancellation_chart=cancellation_trend(data),

        country_chart=country_analysis(data),

        market_chart=market_analysis(data),

        season_chart=season_analysis(data),

        lead_histogram=lead_histogram(data),

        adr_chart=adr_distribution(data),

        scatter_chart=lead_vs_adr(data),

        stay_chart=stay_duration(data),

        guest_chart=guest_chart(data),

        heatmap=correlation_heatmap(data),
        insights = generate_insights(data)

    )


@app.route("/booking")
def booking():

    hotel = request.args.get("hotel","All")

    country = request.args.get("country","All")

    segment = request.args.get("segment","All")

    df = load_dataset()

    data = filter_booking_data(
        df,
        hotel,
        country,
        segment
    )

    kpi = {

        "total": len(data),

        "cancelled": int(data["is_canceled"].sum()),

        "confirmed": len(data) - int(data["is_canceled"].sum()),

        "lead": round(data["lead_time"].mean(), 1),

        "adr": round(data["adr"].mean(), 2),

        "stay": round(data["total_stay"].mean(), 2),

        "guests": int(data["total_guests"].sum()),

        "revenue": round(data["average_daily_revenue"].sum(), 2)

    }

    return render_template(

        "booking.html",

        kpi=kpi,

        hotel=hotel,

        country=country,

        segment=segment,

        hotels=["All"] +
        sorted(df["hotel"].unique()),

        countries=["All"] +
        sorted(df["country"].unique()),

        segments=["All"] +
        sorted(df["market_segment"].unique()),

        chart1=monthly_booking_chart(data),

        chart2=hotel_type_chart(data),

        chart3=country_booking_chart(data),

        chart4=market_segment_chart(data),
        booking_season_chart=booking_season_chart(data),

        lead_time_chart=lead_time_chart(data),

        cancellation_month_chart=cancellation_month_chart(data),

        booking_heatmap=booking_heatmap(data),

        booking_scatter=booking_scatter(data),

        booking_box=booking_box(data),

        table=data.head(30).to_html(
            classes="table table-hover table-striped",
            index=False
        )

    )



@app.route("/customer")
def customer():
    df = load_dataset()

    return render_template(

        "customer.html",

        hotels=["All"] + sorted(df.hotel.unique()),

        countries=["All"] + sorted(df.country.unique()),

        customers=["All"] + sorted(df.customer_type.unique()),

        kpi={

            "total": len(df),

            "repeat": int(df.is_repeated_guest.sum()),

            "new": len(df) - int(df.is_repeated_guest.sum()),

            "adults": int(df.adults.sum()),

            "children": int(df.children.sum()),

            "babies": int(df.babies.sum())

        },

        customer=customer_chart(df),

        repeat=repeat_guest_chart(df),

        guest=guest_demographics(df),

        request_chart=special_request_chart(df),

        country_chart=customer_country_chart(df),

        segment_chart=customer_segment_chart(df),

        box_chart=customer_box(df),

        scatter_chart=customer_scatter(df),

        table=df.head(30).to_html(

            classes="table table-hover table-striped",

            index=False

        )

    )


@app.route("/revenue")
def revenue():

    df = load_dataset()

    revenue_df = df.copy()
    revenue_df["Revenue"] = revenue_df["adr"] * revenue_df["total_stay"]

    weekend = revenue_df[revenue_df["weekend_stay"] == 1]["Revenue"].sum()
    weekday = revenue_df[revenue_df["weekend_stay"] == 0]["Revenue"].sum()

    hotel = (
        revenue_df.groupby("hotel")["Revenue"]
        .sum()
        .idxmax()
    )

    kpi = {

        "total": round(revenue_df["Revenue"].sum(),2),

        "adr": round(df["adr"].mean(),2),

        "stay": round(df["total_stay"].mean(),2),

        "weekend": round(weekend,2),

        "weekday": round(weekday,2),

        "hotel": hotel

    }

    return render_template(

        "revenue.html",

        kpi=kpi,

        revenue=revenue_chart(df),

        hotel=hotel_revenue_chart(df),

        season=season_revenue_chart(df),

        adr=adr_chart(df),

        hist=revenue_histogram(df),

        weekend=weekend_revenue(df),

        scatter=revenue_scatter(df),

        violin=revenue_violin(df),

        table=revenue_df.head(30).to_html(

            classes="table table-hover table-striped",

            index=False

        )

    )


@app.route("/statistics")
def statistics():

    df = load_dataset()

    return render_template(

        "statistics.html",

        corr=correlation_chart(df),

        qq=qq_plot(df),

        distribution=distribution_chart(df),

        lead=lead_distribution(df),

        stay=stay_distribution(df),

        scatter=lead_vs_stay(df),

        booking_changes=booking_changes_chart(df),

        special=special_requests_chart(df),

        cancel_box=cancellation_box(df),

        density=adr_density(df)

    )


@app.route("/explorer")
def explorer():

    df=load_dataset()

    return render_template(

        "explorer.html",

        table=df.head(100).to_html(

            classes="table table-hover table-striped",

            index=False

        ),

        total=len(df),

        hotels=sorted(df.hotel.unique()),

        countries=sorted(df.country.unique()),

        customers=sorted(df.customer_type.unique()),

        seasons=sorted(df.booking_season.unique())

    )


@app.route("/reports")
def reports():

    return render_template(

        "reports.html"

    )

@app.route("/dashboard/filter")

def dashboard_filter():

    data = load_dataset()

    data = apply_filters(data, request)

    return jsonify({

        "kpis": render_template(
            "components/kpi_cards.html",
            kpi=get_dashboard_kpis(data)
        ),

        "booking_chart": booking_trend(data),

        "hotel_chart": hotel_distribution(data),

        "revenue_chart": revenue_trend(data),

        "country_chart": country_analysis(data),

        "market_chart": market_analysis(data),

        "cancel_chart": cancellation_trend(data),

        "adr_chart": adr_distribution(data),

        "scatter_chart": lead_vs_adr(data),

        "heatmap": correlation_heatmap(data),

        "season_chart": season_analysis(data),

        "lead_chart": lead_histogram(data),

        "guest_chart": guest_chart(data),

        "table": render_template(
            "components/table.html",
            table=data.head(20)
        )

    })
@app.route("/api/dashboard")

def dashboard_api():


    data = load_dataset()
    insights = generate_insights(data)


    data = apply_filters(
        data,
        request
    )


    response={


    "kpi":
    get_dashboard_kpis(data),


    "charts":{


    "booking":
    booking_trend(data),


    "revenue":
    revenue_trend(data),


    "hotel":
    hotel_distribution(data),


    "country":
    country_analysis(data),


    "market":
    market_analysis(data),


    "season":
    season_analysis(data)

    }


    }


    return jsonify(response)
from flask import send_from_directory
import os
@app.route("/download/processed-dataset")
def download_processed_dataset():

    dataset_path = os.path.join(app.root_path, "datasets")

    return send_from_directory(
        dataset_path,
        "processed_hotel_bookings.csv",
        as_attachment=True
    )
@app.route("/download/cleaned-dataset")
def download_cleaned_dataset():

    dataset_path = os.path.join(app.root_path, "datasets")

    return send_from_directory(
        dataset_path,
        "cleaned_hotel_bookings.csv",
        as_attachment=True
    )

@app.route("/notebooks")
def notebooks():

    notebook_folder = os.path.abspath(
        os.path.join(
            app.root_path,
            "..",
            "notebooks"
        )
    )

    files = sorted(

        file

        for file in os.listdir(notebook_folder)

        if file.endswith(".ipynb")

    )

    return render_template(

        "notebooks.html",

        notebooks=files

    )
@app.route("/download/notebook/<filename>")
def download_notebook(filename):

    notebook_folder = os.path.abspath(
        os.path.join(
            app.root_path,
            "..",
            "notebooks"
        )
    )

    return send_from_directory(

        notebook_folder,

        filename,

        as_attachment=True

    )

if __name__ == "__main__":

    app.run(
        debug=True
    )

