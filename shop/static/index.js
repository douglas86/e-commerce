// get localStorage item cart
// if doesn't exist create it
if (localStorage.getItem("cart") == null) {
  var cart = {};
} else {
  cart = JSON.parse(localStorage.getItem("cart"));
}

// once item is clicked
$(document).on("click", ".atc", function () {
  var item_id = this.id.toString();
  if (cart[item_id] != undefined) {
    cart[item_id] = cart[item_id] + 1;
  } else {
    cart[item_id] = 1;
  }
  localStorage.setItem("cart", JSON.stringify(cart));
  document.getElementById("cart").innerHTML =
    "Cart(" + Object.keys(cart).length + ")";
  location.reload();
});

// run function
displayCart(cart);

// create items in popover menu
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

// load function when doc starts
function loadFun(cart) {
  for (var x in cart) {
    document.getElementById("cart").innerHTML =
      "Cart(" + Object.keys(cart).length + ")";
  }
}

// start loading on windows start
$(window).on("load", loadFun(cart));
