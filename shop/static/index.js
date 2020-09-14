console.log("this is working");

if (localStorage.getItem("cart") == null) {
  var cart = {};
} else {
  cart = JSON.parse(localStorage.getItem("cart"));
}

$(document).on("click", ".atc", function () {
  console.log("The add to button is clicked");
});
