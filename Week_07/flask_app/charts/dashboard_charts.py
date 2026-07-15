import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

# -----------------------------------------------------
# Common Layout
# -----------------------------------------------------

def style(fig, title):

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

# -----------------------------------------------------
# Booking Trend
# -----------------------------------------------------
import pandas as pd
def booking_trend(df):

    data = df.groupby("arrival_date_month").size().reset_index(name="Bookings")

    fig = px.line(
        data,
        x="arrival_date_month",
        y="Bookings",
        markers=True
    )

    return style(fig, "Monthly Booking Trend")

    fig = px.bar(
        data,
        x="arrival_date_month",
        y="Bookings",
        color="Bookings",
        color_continuous_scale="Purples"
    )

    fig.update_layout(
        showlegend=False,
        coloraxis_showscale=False
    )

    return style(fig, "Monthly Booking Trend")


# -----------------------------------------------------
# Revenue Trend
# -----------------------------------------------------

def revenue_trend(df):

    revenue=df.copy()

    revenue["Revenue"]=revenue["adr"]*revenue["total_stay"]

    revenue=revenue.groupby(
        "arrival_date_month"
    )["Revenue"].sum().reset_index()

    fig = px.area(
        revenue,
        x="arrival_date_month",
        y="Revenue",
        color_discrete_sequence=["#A855F7"]
    )

    fig.update_traces(
        fillcolor="rgba(192,132,252,0.35)"
    )

    return style(fig,"Revenue Trend")

purple_colors = [
    "#C084FC",
    "#A855F7",
    "#7E22CE",
    "#E879F9",
    "#F0ABFC"
]
# -----------------------------------------------------
# Hotel Distribution
# -----------------------------------------------------

def hotel_distribution(df):

    fig=px.pie(

        df,

        names="hotel",

        hole=.45,
        color_discrete_sequence=purple_colors

    )

    return style(fig,"Hotel Type Distribution")


# -----------------------------------------------------
# Cancellation Trend
# -----------------------------------------------------

def cancellation_trend(df):

    data=df.groupby(
        "arrival_date_month"
    )["is_canceled"].mean().reset_index()

    data["is_canceled"]*=100

    fig=px.bar(

        data,

        x="arrival_date_month",

        y="is_canceled",
        color_discrete_sequence=["#C084FC"]

    )

    return style(fig,"Cancellation Rate")


# -----------------------------------------------------
# Country Analysis
# -----------------------------------------------------

def country_analysis(df):

    data=df.country.value_counts().head(10)

    fig=px.bar(

        x=data.index,

        y=data.values,

        labels={"x":"Country","y":"Bookings"},
        color_discrete_sequence=["#C084FC"]

    )

    return style(fig,"Top Countries")


# -----------------------------------------------------
# Market Segment
# -----------------------------------------------------

def market_analysis(df):

    data=df.market_segment.value_counts()

    fig=px.bar(

        x=data.index,

        y=data.values,
        color_discrete_sequence=["#C084FC"]

    )

    return style(fig,"Market Segment")


# -----------------------------------------------------
# Season Analysis
# -----------------------------------------------------

def season_analysis(df):

    data=df.booking_season.value_counts()

    fig=px.pie(

        names=data.index,

        values=data.values,

        hole=.4,
        color_discrete_sequence=purple_colors

    )

    return style(fig,"Booking Season")


# -----------------------------------------------------
# Lead Histogram
# -----------------------------------------------------

def lead_histogram(df):

    fig=px.histogram(

        df,

        x="lead_time",

        nbins=40,
        color_discrete_sequence=["#C084FC"]

    )
    fig.update_traces(
        marker_line_color="#FFFFFF",
        marker_line_width=0.5
    )

    return style(fig,"Lead Time Distribution")


# -----------------------------------------------------
# ADR Distribution
# -----------------------------------------------------

def adr_distribution(df):
    fig = px.box(
        df,
        y="adr",
        color="hotel",
        color_discrete_sequence=purple_colors
    )

    fig.update_traces(
        line=dict(
            color="white"
        )
    )

    return style(fig,"Average Daily Rate")


# -----------------------------------------------------
# Lead vs ADR
# -----------------------------------------------------

def lead_vs_adr(df):

    fig=px.scatter(

        df,

        x="lead_time",

        y="adr",

        color="hotel",

        opacity=.7,
        color_discrete_sequence=purple_colors

    )
    fig.update_traces(
        marker=dict(
            size=8,
            line=dict(
                color="white",
                width=0.5
            )
        )
    )

    return style(fig,"Lead Time vs ADR")


# -----------------------------------------------------
# Stay Duration
# -----------------------------------------------------

def stay_duration(df):

    fig=px.histogram(

        df,

        x="total_stay",

        nbins=25,
        color_discrete_sequence=["#C084FC"]

    )
    fig.update_traces(
        marker_line_color="#FFFFFF",
        marker_line_width=0.5
    )

    return style(fig,"Stay Duration")


# -----------------------------------------------------
# Guest Chart
# -----------------------------------------------------

def guest_chart(df):

    guests={

        "Adults":df.adults.sum(),

        "Children":df.children.sum(),

        "Babies":df.babies.sum()

    }

    fig=px.bar(

        x=list(guests.keys()),

        y=list(guests.values()),
        color_discrete_sequence=["#C084FC"]

    )

    return style(fig,"Guest Distribution")


# -----------------------------------------------------
# Correlation Heatmap
# -----------------------------------------------------

def correlation_heatmap(df):

    cols=[

        "lead_time",

        "adr",

        "total_stay",

        "total_guests",

        "booking_changes",

        "previous_cancellations",

        "previous_bookings_not_canceled",

        "total_of_special_requests"

    ]

    corr=df[cols].corr().round(2)

    fig=ff.create_annotated_heatmap(

        z=corr.values,

        x=list(corr.columns),

        y=list(corr.index),

        colorscale=[
            [0, "#1E1035"],
            [0.3, "#7E22CE"],
            [0.6, "#C084FC"],
            [1, "#F0ABFC"]
        ]

    )

    fig.update_layout(

        autosize=True,

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        ),

        width=None,

        height=420,

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)"
    )
    fig.update_traces(
        textfont=dict(
            color="white"
        )
    )
    return fig.to_html(
        full_html=False,
        include_plotlyjs=False,
        config={
            "responsive": True
        }
    )