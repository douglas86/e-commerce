if (localStorage.getItem("cart") == null) {
  var cart = {};
} else {
  cart = JSON.parse(localStorage.getItem("cart"));
}

$(document).on("click", ".atc", function () {
  var item_id = this.id.toString();
  console.log(item_id);
  if (cart[item_id] != undefined) {
    cart[item_id] = cart[item_id] + 1;
  } else {
    cart[item_id] = 1;
  }
  console.log(cart);
  localStorage.setItem("cart", JSON.stringify(cart));
});

$(function () {
  $('[data-toggle="popover"]').popover();
});

displayCart(cart);

function displayCart(cart) {
  console.log("this is the cart" + cart);
  cartString = "";
  cartString += "<h5>This is the cart</h5>";
  console.log(cartString);
}
