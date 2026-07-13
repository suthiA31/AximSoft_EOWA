const counters=document.querySelectorAll(".counter");

counters.forEach(counter=>{

const update=()=>{

const target=+counter.getAttribute("data-target");

const c=+counter.innerText;

const inc=target/200;

if(c<target){

counter.innerText=Math.ceil(c+inc);

setTimeout(update,8);

}

else{

counter.innerText=target.toLocaleString();

}

}

update();

});