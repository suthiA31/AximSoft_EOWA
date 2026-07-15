// =====================================
// Dashboard Dynamic Filter System
// =====================================


function loadDashboardData(){

    let hotel =
    document.querySelector("#hotel").value;


    let country =
    document.querySelector("#country").value;


    let market =
    document.querySelector("#market").value;


    let customer =
    document.querySelector("#customer").value;


    let season =
    document.querySelector("#season").value;



    let params =
    new URLSearchParams({

        hotel:hotel,

        country:country,

        market:market,

        customer:customer,

        season:season

    });



    document
    .getElementById("loader")
    .style.display="flex";



    fetch(
        "/api/dashboard?"
        +
        params.toString()

    )

    .then(response=>response.json())


    .then(data=>{


        // Update KPI cards

        document
        .getElementById("totalBookings")
        .innerHTML=data.kpi.total_bookings;


        document
        .getElementById("cancelRate")
        .innerHTML=data.kpi.cancellation_rate+"%";


        document
        .getElementById("adr")
        .innerHTML=data.kpi.adr;



        // Update Charts

        document
        .getElementById("bookingChart")
        .innerHTML=data.charts.booking;


        document
        .getElementById("revenueChart")
        .innerHTML=data.charts.revenue;


        document
        .getElementById("hotelChart")
        .innerHTML=data.charts.hotel;


        document
        .getElementById("countryChart")
        .innerHTML=data.charts.country;



        document
        .getElementById("marketChart")
        .innerHTML=data.charts.market;



        document
        .getElementById("seasonChart")
        .innerHTML=data.charts.season;



        document
        .getElementById("loader")
        .style.display="none";


    })

}



// Auto refresh when filter changes


document
.querySelectorAll(".dashboard-filter")
.forEach(

element=>{

element
.addEventListener(

"change",

loadDashboardData

);

}

);