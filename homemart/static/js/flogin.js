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
  fetch("https://api.opencagedata.com/geocode/v1/json?q=${latitude}+${longitude}&key=5400eb06e9ee4ca7851639e6b632f55f")
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


