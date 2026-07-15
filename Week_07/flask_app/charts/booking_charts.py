import plotly.express as px
import pandas as pd
purple_colors = [
    "#C084FC",
    "#A855F7",
    "#7E22CE",
    "#E879F9",
    "#F0ABFC"
]
def layout(fig, title):

    fig.update_layout(

        title=dict(
            text=title,
            x=0.5,
            font=dict(
                color="#FFFFFF",
                size=22
            )
        ),

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.05)",

        font=dict(
            color="#FFFFFF",
            size=14
        ),

        xaxis=dict(
            color="#FFFFFF",
            tickfont=dict(
                color="#FFFFFF",
                size=12
            ),
            title_font=dict(
                color="#FFFFFF"
            ),
            gridcolor="rgba(255,255,255,0.15)"
        ),

        yaxis=dict(
            color="#FFFFFF",
            tickfont=dict(
                color="#FFFFFF",
                size=12
            ),
            title_font=dict(
                color="#FFFFFF"
            ),
            gridcolor="rgba(255,255,255,0.15)"
        ),

        legend=dict(
            font=dict(
                color="#FFFFFF"
            )
        ),

        margin=dict(
            l=30,
            r=30,
            t=70,
            b=30
        ),

        height=420
    )


    return fig.to_html(

        full_html=False,

        include_plotlyjs=False,

        config={
            "responsive":True
        }

    )

# ------------------------------------------------
# Monthly Booking
# ------------------------------------------------

def monthly_booking_chart(df):

    data = df.groupby("arrival_date_month").size().reset_index(name="Bookings")

    fig = px.line(
        data,
        x="arrival_date_month",
        y="Bookings",
        markers=True
    )

    return layout(fig, "Monthly Booking Trend")

    data=data.sort_values("arrival_date_month")

    fig=px.line(

        data,

        x="arrival_date_month",

        y="Bookings",

        markers=True,
        color_discrete_sequence=["#C084FC"]

    )

    return layout(fig,"Monthly Booking Trend")


# ------------------------------------------------

def hotel_type_chart(df):

    data=df.hotel.value_counts().reset_index()

    data.columns=["Hotel","Bookings"]

    fig=px.bar(

        data,

        x="Hotel",

        y="Bookings",

        color="Hotel",
        color_discrete_sequence=["#C084FC"]

    )

    return layout(fig,"Hotel Type Comparison")


# ------------------------------------------------

def country_booking_chart(df):

    data=df.country.value_counts().head(10).reset_index()

    data.columns=["Country","Bookings"]

    fig=px.bar(

        data,

        x="Country",

        y="Bookings",

        color="Bookings",
        color_discrete_sequence=["#C084FC"]

    )

    return layout(fig,"Top Countries")


# ------------------------------------------------

def market_segment_chart(df):

    data=df.market_segment.value_counts().reset_index()

    data.columns=["Segment","Bookings"]

    fig=px.pie(

        data,

        names="Segment",

        values="Bookings",

        hole=.45,
        color_discrete_sequence=purple_colors

    )

    return layout(fig,"Market Segment")


# ------------------------------------------------

def booking_season_chart(df):

    data=df.booking_season.value_counts().reset_index()

    data.columns=["Season","Bookings"]

    fig=px.bar(

        data,

        x="Season",

        y="Bookings",

        color_discrete_sequence=["#C084FC"]

    )

    return layout(fig,"Booking Season")


# ------------------------------------------------

def lead_time_chart(df):

    fig=px.histogram(

        df,

        x="lead_time",

        nbins=40,

        color_discrete_sequence=["#C084FC"]

    )

    return layout(fig,"Lead Time Distribution")


# ------------------------------------------------

def cancellation_month_chart(df):

    data=df.groupby(

        "arrival_date_month"

    )["is_canceled"].mean().reset_index()

    fig=px.line(

        data,

        x="arrival_date_month",

        y="is_canceled",

        markers=True,
        color_discrete_sequence=["#C084FC"]

    )

    return layout(fig,"Cancellation Trend")


# ------------------------------------------------

def booking_heatmap(df):

    pivot=df.pivot_table(

        values="adr",

        index="hotel",

        columns="booking_season",

        aggfunc="mean"

    )

    fig=px.imshow(

        pivot,

        text_auto=True,

        aspect="auto"

    )

    return layout(fig,"Hotel vs Season ADR")


# ------------------------------------------------

def booking_scatter(df):

    fig=px.scatter(

        df,

        x="lead_time",

        y="adr",

        color="hotel",
        color_discrete_sequence=purple_colors

    )

    return layout(fig,"Lead Time vs ADR")


# ------------------------------------------------

def booking_box(df):

    fig=px.box(

        df,

        x="hotel",

        y="lead_time",

        color="hotel",
        color_discrete_sequence=purple_colors

    )

    return layout(fig,"Lead Time by Hotel")