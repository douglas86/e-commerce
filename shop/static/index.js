if (localStorage.getItem("cart") == null) {
  var cart = {};
} else {
  cart = JSON.parse(localStorage.getItem("cart"));
}

$(document).on("click", ".atc", function () {
  var item_id = this.id.toString();
<<<<<<< HEAD
  // console.log(item_id);
=======
  console.log(item_id);
>>>>>>> navbar
  if (cart[item_id] != undefined) {
    cart[item_id] = cart[item_id] + 1;
  } else {
    cart[item_id] = 1;
  }
<<<<<<< HEAD
  // console.log(cart);
=======
  console.log(cart);
>>>>>>> navbar
  localStorage.setItem("cart", JSON.stringify(cart));
  document.getElementById("cart").innerHTML =
    "Cart(" + Object.keys(cart).length + ")";
});

<<<<<<< HEAD
DisplayCart(cart);

function DisplayCart(cart) {
  var cartString = "";
  cartString += "<h5>This is your cart</h5>";
  var cartIndex = 1;
  for (var x in cart) {
    cartString += cartIndex;
    cartString +=
      document.getElementById("nm" + x).innerHTML + "Qty:" + cart[x] + "<br>";
    cartIndex += 1;
  }

  cartString += "<button>checkout</button>";
=======
$(function () {
  $('[data-toggle="popover"]').popover();
});

displayCart(cart);

function displayCart(cart) {
  cartString = "";
  cartString += "<h5>This is the cart</h5>";
  cartIndex = 1;
  for (var x in cart) {
    cartString += cartIndex;
    cartString +=
		  document.getElementById("nm" + x).innerHTML + "Qty: " + cart[x] + "<br>";
    cartIndex += 1;
  }
  cartString +=
    "<a href='/checkout'>Checkout</a>";
>>>>>>> navbar
  document.getElementById("cart").setAttribute("data-content", cartString);
  $('[data-toggle="popover"]').popover();
}
