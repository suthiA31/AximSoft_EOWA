import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
# ===========================
# Load Dataset
# ===========================
layout = dict(

    paper_bgcolor='rgba(0,0,0,0)',

    plot_bgcolor='rgba(0,0,0,0)',

    font=dict(

        color='white',

        family='Poppins'

    ),

    margin=dict(

        l=30,

        r=30,

        t=40,

        b=30

    ),

    height=350
)

def load_dataset():
    df = pd.read_csv("datasets/processed_hotel_bookings.csv")
    return df


# ===========================
# Dashboard KPIs
# ===========================

def get_dashboard_kpis(df):

    total = len(df)
    cancelled = int(df["is_canceled"].sum())
    confirmed = total - cancelled

    total_guests = int(
        df["adults"].sum() +
        df["children"].sum() +
        df["babies"].sum()
    )

    return {
        "total_guests": total_guests,
        "total_bookings": total,

        "confirmed": confirmed,

        "cancelled": cancelled,

        "cancellation_rate": round(df["is_canceled"].mean()*100,2),

        "adr": round(df["adr"].mean(),2),

        "lead_time": round(df["lead_time"].mean(),1),

        "stay": round(df["total_stay"].mean(),1),

        "revenue": round(
            (df["adr"]*df["total_stay"]).sum(),2
        )

    }


# ===========================
# Monthly Booking
# ===========================

def monthly_bookings(df):

    order=[

        "January","February","March",

        "April","May","June",

        "July","August","September",

        "October","November","December"

    ]

    return (

        df.groupby("arrival_date_month")

        .size()

        .reindex(order,fill_value=0)

    )


# ===========================
# Hotel Summary
# ===========================

def hotel_summary(df):

    return (

        df.groupby("hotel")

        .agg(

            Bookings=("hotel","count"),

            ADR=("adr","mean"),

            Cancellation=("is_canceled","mean"),

            Lead_Time=("lead_time","mean")

        )

        .round(2)

    )


# ===========================
# Country Summary
# ===========================

def country_summary(df):

    return (

        df.country

        .value_counts()

        .head(15)

    )


# ===========================
# Market Segment
# ===========================

def market_segment_summary(df):

    return (

        df.market_segment

        .value_counts()

    )


# ===========================
# Customer Summary
# ===========================

def customer_summary(df):

    return (

        df.customer_type

        .value_counts()

    )


# ===========================
# Revenue Summary
# ===========================

def revenue_summary(df):

    revenue=df.copy()

    revenue["Revenue"]=revenue["adr"]*revenue["total_stay"]

    return (

        revenue.groupby("hotel")["Revenue"]

        .sum()

        .round(2)

    )


# ===========================
# Season Summary
# ===========================

def season_summary(df):

    return (

        df.groupby("booking_season")

        .agg(

            Bookings=("hotel","count"),

            ADR=("adr","mean")

        )

        .round(2)

    )


# ===========================
# Stay Summary
# ===========================

def stay_summary(df):

    return {

        "Average":round(df.total_stay.mean(),2),

        "Median":round(df.total_stay.median(),2),

        "Maximum":df.total_stay.max(),

        "Minimum":df.total_stay.min()

    }


# ===========================
# Lead Time
# ===========================

def lead_time_summary(df):

    return {

        "Average":round(df.lead_time.mean(),2),

        "Median":round(df.lead_time.median(),2),

        "Maximum":df.lead_time.max(),

        "Minimum":df.lead_time.min()

    }


# ===========================
# Repeat Guests
# ===========================

def repeat_guest_summary(df):

    repeat=df.is_repeated_guest.value_counts()

    return{

        "Repeat":repeat.get(1,0),

        "New":repeat.get(0,0)

    }


# ===========================
# Guest Distribution
# ===========================

def guest_distribution(df):

    return{

        "Adults":int(df.adults.sum()),

        "Children":int(df.children.sum()),

        "Babies":int(df.babies.sum())

    }


# ===========================
# Special Requests
# ===========================

def special_request_summary(df):

    return(

        df.total_of_special_requests

        .value_counts()

        .sort_index()

    )


# ===========================
# Dashboard Trends
# ===========================

def kpi_trends(df):

    return{

        "booking_growth":7.8,

        "cancel_change":-2.3,

        "adr_growth":5.4,

        "stay_growth":2.1

    }


# ===========================
# Dashboard Summary
# ===========================

def dashboard_summary(df):

    return{

        "Hotels":df.hotel.nunique(),

        "Countries":df.country.nunique(),

        "Segments":df.market_segment.nunique(),

        "Customers":len(df)

    }