function check() {
  var checkbox = document.getElementById("flexCheckDefault");
  if (checkbox.checked) {
    let button = document.getElementById("button");
    button.type = "submit";
  }
  else {
    alert("please check this ckeck button ")
    let button = document.getElementById("button");
    button.type = "button";
  }
}


function clear_form() {
  document.getElementById("exampleEmail").value = '';
  document.getElementById("examplePassword").value = '';
  document.getElementById("exampleNewPassword").value = '';
  document.getElementById("otp").value = '';
}
window.onload = clear_form;



