import plotly.express as px
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


# -----------------------------------------------

def customer_chart(df):

    data=df.customer_type.value_counts().reset_index()

    data.columns=["Customer","Count"]

    fig=px.pie(

        data,

        names="Customer",

        values="Count",

        hole=.45,
        color_discrete_sequence=purple_colors

    )

    return layout(fig,"Customer Type Distribution")


# -----------------------------------------------

def repeat_guest_chart(df):

    data=df.is_repeated_guest.value_counts().reset_index()

    data.columns=["Repeat","Guests"]

    data["Repeat"]=data["Repeat"].replace({

        0:"New",

        1:"Repeat"

    })

    fig=px.bar(

        data,

        x="Repeat",

        y="Guests",

        color="Repeat",
        color_discrete_sequence=["#C084FC"]

    )

    return layout(fig,"Repeat Guests")


# -----------------------------------------------

def guest_demographics(df):

    values=[

        df.adults.sum(),

        df.children.sum(),

        df.babies.sum()

    ]

    fig=px.bar(

        x=["Adults","Children","Babies"],

        y=values,

        color=["Adults","Children","Babies"],
        color_discrete_sequence=["#C084FC"]

    )

    return layout(fig,"Guest Demographics")


# -----------------------------------------------

def special_request_chart(df):

    data=df.total_of_special_requests.value_counts().sort_index()

    fig=px.bar(

        x=data.index,

        y=data.values,
        color_discrete_sequence=["#C084FC"]

    )

    return layout(fig,"Special Requests")


# -----------------------------------------------

def customer_country_chart(df):

    data=df.country.value_counts().head(15)

    fig=px.bar(

        x=data.index,

        y=data.values,

        color=data.values,
        color_discrete_sequence=["#C084FC"]

    )

    return layout(fig,"Country-wise Customers")


# -----------------------------------------------

def customer_segment_chart(df):

    data=df.groupby(

        "market_segment"

    ).size().reset_index(name="Bookings")

    fig=px.treemap(

        data,

        path=["market_segment"],

        values="Bookings",
        color_discrete_sequence=purple_colors

    )

    return layout(fig,"Customer Market Segment")


# -----------------------------------------------

def customer_box(df):

    fig=px.box(

        df,

        x="customer_group",

        y="adr",

        color="customer_group",
        color_discrete_sequence=purple_colors

    )

    return layout(fig,"Customer Group ADR")


# -----------------------------------------------

def customer_scatter(df):

    fig=px.scatter(

        df,

        x="lead_time",

        y="total_stay",

        color="customer_group",
        color_discrete_sequence=purple_colors

    )

    return layout(fig,"Lead Time vs Stay")