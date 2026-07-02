const chartCanvas =
document.getElementById("dashboardChart");

if(chartCanvas){

new Chart(chartCanvas,{

type:"bar",

data:{

labels:[
"Applied",
"Shortlisted",
"Interview",
"Selected"
],

datasets:[{

label:"Applications",

data:[12,8,5,2]

}]

}

});

}