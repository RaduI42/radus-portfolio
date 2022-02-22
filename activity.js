// Get the container element
var btnContainer = document.getElementById("mainNav");

// Get all buttons with class="btn" inside the container
var btns = btnContainer.getElementsByClassName("nav-item");

// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}

      function myFunction() {
        alert("Page is loaded");
      }
   function mySubmit() {
     alert("The form is submitted");
   }
   function myResize() {
    var w = window.outerWidth;
    var h = window.outerHeight;
    var txt = "Window size: width=" + w + ", height=" + h;
    document.getElementById("demo").innerHTML = txt;
  }
  function lightInput(elm){
    elm.style.background = "grey";
  }