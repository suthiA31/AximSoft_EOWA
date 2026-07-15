import pandas as pd
import numpy as np


def generate_insights(df):

    insights = []

    # -------------------------------
    # Cancellation Rate
    # -------------------------------

    cancel_rate = round(df["is_canceled"].mean()*100,2)

    if cancel_rate > 35:

        insights.append({
            "type":"danger",
            "title":"High Cancellation Rate",
            "message":f"{cancel_rate}% of bookings are cancelled. Consider stricter cancellation policies."
        })

    else:

        insights.append({
            "type":"success",
            "title":"Healthy Cancellation Rate",
            "message":f"Only {cancel_rate}% bookings are cancelled."
        })


    # -------------------------------
    # Highest Revenue Hotel
    # -------------------------------

    revenue = df.groupby("hotel")["adr"].mean()

    best_hotel = revenue.idxmax()

    value = round(revenue.max(),2)

    insights.append({

        "type":"primary",

        "title":"Top Revenue Hotel",

        "message":f"{best_hotel} generates the highest ADR (${value})."

    })


    # -------------------------------
    # Highest Booking Month
    # -------------------------------

    month = (

        df.groupby("arrival_date_month")

        .size()

        .sort_values(ascending=False)

    )

    insights.append({

        "type":"info",

        "title":"Peak Booking Month",

        "message":f"{month.index[0]} recorded the highest number of bookings."

    })


    # -------------------------------
    # Highest Booking Country
    # -------------------------------

    country = (

        df.country

        .value_counts()

    )

    insights.append({

        "type":"success",

        "title":"Top Customer Country",

        "message":f"Most bookings come from {country.index[0]}."

    })


    # -------------------------------
    # Lead Time
    # -------------------------------

    lead = round(df["lead_time"].mean(),1)

    insights.append({

        "type":"warning",

        "title":"Average Lead Time",

        "message":f"Guests book approximately {lead} days before arrival."

    })


    # -------------------------------
    # Repeat Guests
    # -------------------------------

    repeat = round(df["is_repeated_guest"].mean()*100,2)

    insights.append({

        "type":"secondary",

        "title":"Repeat Guests",

        "message":f"{repeat}% customers are repeat guests."

    })


    # -------------------------------
    # Market Segment
    # -------------------------------

    segment = (

        df.market_segment

        .value_counts()

    )

    insights.append({

        "type":"primary",

        "title":"Largest Market Segment",

        "message":f"{segment.index[0]} contributes the highest bookings."

    })


    # -------------------------------
    # Average Stay
    # -------------------------------

    stay = round(df.total_stay.mean(),1)

    insights.append({

        "type":"success",

        "title":"Average Stay",

        "message":f"Guests stay an average of {stay} nights."

    })


    return insights