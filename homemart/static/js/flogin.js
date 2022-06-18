function changeVisibility() {
  document.getElementById("locbtn").style.display = "block";
  }

/*var btn = document.getElementById("locbtn");

btn.addEventListener("click", loc);*/
function loc(){

if (window.navigator.geolocation) {

 window.navigator.geolocation
  .getCurrentPosition(console.log, console.log);

const successfulLookup = position => {
  const { latitude, longitude } = position.coords;
  fetch("https://api.opencagedata.com/geocode/v1/json?q=${latitude}+${longitude}&key=52c7d8f0eac04f7a94a7a2618d7844f7")
    .then(response => {
     const r=response.json();
    return r})
    .then(function (r){console.log(r);
    document.getElementById("location").value = r.results[0].formatted;});
    };

 navigator.geolocation
  .getCurrentPosition(successfulLookup,console.log);
}

}


