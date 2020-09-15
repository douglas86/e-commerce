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
  document.getElementById("cart").innerHTML =
    "Cart(" + Object.keys(cart).length + ")";
});

$(function () {
  $('[data-toggle="popover"]').popover();
	document.getElementById("cart").setAttribute('data-content', '<h5>this is your cart</h5>')
});
