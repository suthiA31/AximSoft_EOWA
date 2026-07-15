import pandas as pd


def apply_filters(df, request):

    filtered = df.copy()

    hotel = request.args.get("hotel")
    country = request.args.get("country")
    market = request.args.get("market")
    customer = request.args.get("customer")
    season = request.args.get("season")
    year = request.args.get("year")

    if hotel and hotel != "All":
        filtered = filtered[filtered["hotel"] == hotel]

    if country and country != "All":
        filtered = filtered[filtered["country"] == country]

    if market and market != "All":
        filtered = filtered[
            filtered["market_segment"] == market
        ]

    if customer and customer != "All":
        filtered = filtered[
            filtered["customer_type"] == customer
        ]

    if season and season != "All":
        filtered = filtered[
            filtered["booking_season"] == season
        ]

    if year and year != "All":

        filtered = filtered[
            filtered["arrival_date_year"].astype(str) == year
        ]

    return filtered


def filter_values(df):

    return {

        "hotels":
        sorted(df.hotel.unique()),

        "countries":
        sorted(df.country.unique()),

        "segments":
        sorted(df.market_segment.unique()),

        "customers":
        sorted(df.customer_type.unique()),

        "years":
        sorted(df.arrival_date_year.unique()),

        "seasons":
        sorted(df.booking_season.unique())

    }
def filter_booking_data(df, hotel="All", country="All", segment="All"):

    data = df.copy()

    if hotel != "All":
        data = data[data["hotel"] == hotel]

    if country != "All":
        data = data[data["country"] == country]

    if segment != "All":
        data = data[data["market_segment"] == segment]

    return data