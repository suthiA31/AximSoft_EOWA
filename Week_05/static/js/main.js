console.log("CareerHub Loaded");

window.addEventListener(
"scroll",
function(){

const navbar =
document.querySelector(
".custom-navbar"
);

if(window.scrollY > 50){

navbar.style.padding =
"10px 0";

}
else{

navbar.style.padding =
"15px 0";

}

});