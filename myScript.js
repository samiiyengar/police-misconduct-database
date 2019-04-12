function onClickAbout(elem) {
      elem.style.background = "white";
      elem.style.display='block';
      elem.height = 100;
      elem.width = 500;
}

function closeForm() {
  document.getElementById("loginPopup").style.display = "none";
  window.location.reload();
}

$(document).ready(function(){
  $('.dropdown-submenu a.test').on("click", function(e){
    $(this).next('ul').toggle();
    e.stopPropagation();
    e.preventDefault();
  });
});

function GoToHomePage()
  {
    window.location = '/';   
  }