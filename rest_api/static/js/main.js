/* Responsive Top Navigation */
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }
  
  /* Sticky Topnav */
  window.onscroll = function() {myFunction()};
  
  var topnav = document.getElementById("myTopnav");
  var sticky = topnav.offsetTop;
  
  function myFunction() {
    if (window.pageYOffset >= sticky) {
      topnav.classList.add("sticky")
    } else {
      topnav.classList.remove("sticky");
    }
  }

  /* Chosen sidenav */ 
  $(document).ready(function(){
    $(".chosen-select").chosen({ max_selected_options: 9 });
  })

  $(document).ready(function(){
    $(".chosen-select").chosen({
      width:'100%'
    });
  });
  
  /* Chosen Nothing Found sidenav */
  $(".chosen-select").chosen({
    no_results_text: "Oops, nothing found!"
  })
  
  /* Sidenav InGroup */
  function toggleNav() {
    var element = document.getElementById("mySidenav");
    if (element.style.width == "200px") {
        element.style.width = "0px";
    } else {
        element.style.width = "200px";
    }
  }

/* New Chat - Select User Functions */
function new_chatFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  function filterFunction() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    div = document.getElementById("myDropdown");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
      txtValue = a[i].textContent || a[i].innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        a[i].style.display = "";
      } else {
        a[i].style.display = "none";
      }
    }
  }

/* Tooltip background */

function percentToRGB(percent) {
    if (percent === 100) {
        percent = 99
    }
    var r, g, b;
    if (percent < 100.5) {
        // green to yellow
        r = Math.floor(255 * (percent / 100.5));
        g = 255;
    } else {
        // yellow to red
        r = 255;
        g = Math.floor(255 * ((100.5 - percent % 100.5) / 100.5));
    }
    b = 0;

    return "rgb(" + r + "," + g + "," + b + ")";
}

function render(value) {

    var x = document.getElementsByClassName("tooltiptext");
    var i;
    for (i = 0; i < x.length; i++) {
      x[i].style.backgroundColor = percentToRGB(value);
  } 
}

/* Limit the number of the users selected for the new group to 9 */
$(document).ready(function(){
    $(".chosen-select").chosen({ max_selected_options: 9 });
  })

let btnClear = document.querySelector('button');
let inputs = document.querySelectorAll('input');

btnClear.addEventListener('click', () => {
    inputs.forEach(input => input.value = '');
});