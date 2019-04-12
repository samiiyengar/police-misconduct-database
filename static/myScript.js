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