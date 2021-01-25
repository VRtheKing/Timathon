var modal = document.getElementById("popupmic");
var modal1 = document.getElementById("popuptext");

var btn = document.getElementById("mike");
var btn1 = document.getElementById("texty");

var span = document.getElementsByClassName("close")[0];
var span1 = document.getElementsByClassName("closee")[0];

btn.onclick = function() {
  modal.style.display = "block";
}

btn1.onclick = function() {
  modal1.style.display = "block";
}

span.onclick = function() {
  modal.style.display = "none";
}

span1.onclick = function() {
  modal1.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

window.onclick = function(event) {
  if (event.target == modal1) {
    modal1.style.display = "none";
  }
}
function start_run(){
  location.href = "/speak";
}
