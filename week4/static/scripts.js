document.addEventListener("DOMContentLoaded", function () {
  var form = document.getElementById("signinForm");
  form.onsubmit = function (event) {
    var checkbox = document.getElementById("remember_me");
    if (!checkbox.checked) {
      event.preventDefault();
      alert("Please check the checkbox first");
    }
  };
});
