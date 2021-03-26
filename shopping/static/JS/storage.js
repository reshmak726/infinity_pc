var overlay = document.querySelector("#overlay");
var close_btn = document.querySelector(".close-overlay");

function on() {
  document.getElementById("overlay").style.display = "flex";
}
close_btn.addEventListener("click", () => {
  off();
});
function off() {
  overlay.style.display = "none";
}
window.onclick = function (event) {
  if (event.target == overlay) {
    off();
  }
};
