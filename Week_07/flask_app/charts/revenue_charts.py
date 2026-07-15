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


# ---------------------------------------
# Revenue Overview
# ---------------------------------------

def revenue_chart(df):

    revenue=df.copy()

    revenue["Revenue"]=revenue["adr"]*revenue["total_stay"]

    data=revenue.groupby(
        "arrival_date_month"
    )["Revenue"].sum().reset_index()

    fig=px.area(
        data,
        x="arrival_date_month",
        y="Revenue",
        color_discrete_sequence=["#A855F7"]

    )

    return layout(fig,"Monthly Revenue")


# ---------------------------------------

def hotel_revenue_chart(df):

    revenue=df.copy()

    revenue["Revenue"]=revenue["adr"]*revenue["total_stay"]

    data=revenue.groupby(
        "hotel"
    )["Revenue"].sum().reset_index()

    fig=px.bar(
        data,
        x="hotel",
        y="Revenue",
        color="hotel",
        color_continuous_scale="Purples"
    )

    return layout(fig,"Revenue by Hotel")


# ---------------------------------------

def season_revenue_chart(df):

    revenue=df.copy()

    revenue["Revenue"]=revenue["adr"]*revenue["total_stay"]

    data=revenue.groupby(
        "booking_season"
    )["Revenue"].sum().reset_index()

    fig=px.pie(
        data,
        names="booking_season",
        values="Revenue",
        hole=.45,
        color_discrete_sequence=purple_colors
    )

    return layout(fig,"Revenue by Season")


# ---------------------------------------

def adr_chart(df):

    fig=px.box(
        df,
        x="hotel",
        y="adr",
        color="hotel",
        color_discrete_sequence=purple_colors
    )

    return layout(fig,"ADR by Hotel")


# ---------------------------------------

def revenue_histogram(df):

    revenue=df.copy()

    revenue["Revenue"]=revenue["adr"]*revenue["total_stay"]

    fig=px.histogram(
        revenue,
        x="Revenue",
        nbins=40,
        color_discrete_sequence=["#C084FC"]
    )

    return layout(fig,"Revenue Distribution")


# ---------------------------------------

def revenue_scatter(df):

    revenue=df.copy()

    revenue["Revenue"]=revenue["adr"]*revenue["total_stay"]

    fig=px.scatter(
        revenue,
        x="lead_time",
        y="Revenue",
        color="hotel",
        color_discrete_sequence=purple_colors
    )

    return layout(fig,"Lead Time vs Revenue")


# ---------------------------------------

def weekend_revenue(df):

    revenue=df.copy()

    revenue["Revenue"]=revenue["adr"]*revenue["total_stay"]

    data=revenue.groupby(
        "weekend_stay"
    )["Revenue"].mean().reset_index()

    fig=px.bar(
        data,
        x="weekend_stay",
        y="Revenue",
        color="weekend_stay",
        color_discrete_sequence = purple_colors,
    )

    return layout(fig,"Weekend Revenue")


# ---------------------------------------

def revenue_violin(df):

    fig=px.violin(
        df,
        x="hotel",
        y="adr",
        color="hotel",
        color_discrete_sequence=purple_colors,
        box=True
    )

    return layout(fig,"ADR Distribution")