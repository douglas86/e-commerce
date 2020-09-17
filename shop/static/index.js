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
    quantity = cart[item_id][0] + 1;
    cart[item_id][0] = quantity;
  } else {
    quantity = 1;
    name = document.getElementById("nm" + item_id).innerHTML;
    cart[item_id] = [quantity, name];
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
      document.getElementById("nm" + x).innerHTML + "Qty: " + cart[0] + "<br>";
    cartIndex += 1;
  }
  cartString += "<a href='/checkout'>Checkout</a>";
  document.getElementById("cart").setAttribute("data-content", cartString);
  $('[data-toggle="popover"]').popover();
  console.log(cart);
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

function check(){
	alert("page")
}
