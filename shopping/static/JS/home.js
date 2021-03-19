// slideshow overlay
var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {
    slideIndex = 1;
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}

// miniSlides
// miniSlide1
var slideIndex = 1;
showDivs1(slideIndex);

function plusDivs1(n) {
  showDivs1((slideIndex += n));
}

function showDivs1(n) {
  var i;
  var x = document.getElementsByClassName("miniSlides1");
  if (n > x.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = x.length;
  }
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  x[slideIndex - 1].style.display = "block";
}

// miniSlide2

var slideIndex = 1;
showDivs2(slideIndex);

function plusDivs2(n) {
  showDivs2((slideIndex += n));
}

function showDivs2(n) {
  var i;
  var x = document.getElementsByClassName("miniSlides2");
  if (n > x.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = x.length;
  }
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  x[slideIndex - 1].style.display = "block";
}

// miniSlide3

var slideIndex = 1;
showDivs3(slideIndex);

function plusDivs3(n) {
  showDivs3((slideIndex += n));
}

function showDivs3(n) {
  var i;
  var x = document.getElementsByClassName("miniSlides3");
  if (n > x.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = x.length;
  }
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  x[slideIndex - 1].style.display = "block";
}
