import plotly.express as px
import plotly.figure_factory as ff
import scipy.stats as stats
import numpy as np
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

def correlation_chart(df):

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

    corr=df[cols].corr()

    fig=ff.create_annotated_heatmap(

        z=corr.values,

        x=list(corr.columns),

        y=list(corr.index),

        colorscale="Viridis",


    )

    fig.update_layout(title="Correlation Matrix")
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

    return fig.to_html(
        full_html=False,
        include_plotlyjs=False,
        config={"responsive": True}
    )


# ---------------------------------------

def distribution_chart(df):

    fig=px.histogram(

        df,

        x="adr",

        marginal="box",

        nbins=40,
        color_discrete_sequence=purple_colors

    )

    return layout(fig,"ADR Distribution")


# ---------------------------------------

def qq_plot(df):

    sample=np.sort(df["adr"].dropna())

    theoretical=stats.norm.ppf(

        np.linspace(.01,.99,len(sample))

    )

    fig=px.scatter(

        x=theoretical,

        y=sample,


    )

    fig.update_layout(

        xaxis_title="Theoretical Quantiles",

        yaxis_title="Sample Quantiles"

    )

    return layout(fig,"QQ Plot")


# ---------------------------------------

def lead_distribution(df):

    fig=px.histogram(

        df,

        x="lead_time",

        nbins=35,
        color_discrete_sequence=purple_colors

    )

    return layout(fig,"Lead Time Distribution")


# ---------------------------------------

def stay_distribution(df):

    fig=px.histogram(

        df,

        x="total_stay",

        nbins=30,

        color_discrete_sequence=purple_colors

    )

    return layout(fig,"Stay Distribution")


# ---------------------------------------

def booking_changes_chart(df):

    fig=px.box(

        df,

        y="booking_changes",
        color_discrete_sequence=purple_colors

    )

    return layout(fig,"Booking Changes")


# ---------------------------------------

def special_requests_chart(df):

    fig=px.histogram(

        df,

        x="total_of_special_requests",
        color_discrete_sequence=purple_colors

    )

    return layout(fig,"Special Requests")


# ---------------------------------------

def cancellation_box(df):

    fig=px.box(

        df,

        x="reservation_status",

        y="lead_time",
        color_discrete_sequence=purple_colors

    )

    return layout(fig,"Reservation vs Lead Time")


# ---------------------------------------

def lead_vs_stay(df):

    fig=px.scatter(

        df,

        x="lead_time",

        y="total_stay",

        color="hotel",
        color_discrete_sequence=purple_colors

    )

    return layout(fig,"Lead Time vs Stay")


# ---------------------------------------

def adr_density(df):

    fig=px.violin(

        df,

        y="adr",

        color="hotel",

        box=True,
        color_discrete_sequence=purple_colors

    )

    return layout(fig,"ADR Density")