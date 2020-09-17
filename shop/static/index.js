if (localStorage.getItem("cart") == null) {
  var cart = {};
} else {
  cart = JSON.parse(localStorage.getItem("cart"));
}

$(document).on("click", ".atc", function () {
  var item_id = this.id.toString();
  // console.log(item_id);
  console.log(item_id);
  if (cart[item_id] != undefined) {
    cart[item_id] = cart[item_id] + 1;
  } else {
    cart[item_id] = 1;
  }
  // console.log(cart);
  console.log(cart);
  localStorage.setItem("cart", JSON.stringify(cart));
  document.getElementById("cart").innerHTML =
    "Cart(" + Object.keys(cart).length + ")";
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
  cartString += "<a href='/checkout'>Checkout</a>";
  document.getElementById("cart").setAttribute("data-content", cartString);
  $('[data-toggle="popover"]').popover();
}

function loadFun(cart) {
  console.log("I am here");
  for (var x in cart) {
    document.getElementById("cart").innerHTML =
      "Cart(" + Object.keys(cart).length + ")";
  }
}

$(window).on("load", loadFun(cart));
