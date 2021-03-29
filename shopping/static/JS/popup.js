var id = document
overlay = document.getElementById("overlay");
function on() {
  document.getElementById("overlay").style.display = "flex";
}

function off() {
  document.getElementById("overlay").style.display = "none";
}
window.onclick = function (event) {
  if (event.target == overlay) {
  