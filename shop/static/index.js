// get localStorage item cart
// if doesn't exist create it
if (localStorage.getItem("cart") == null) {
  let cart = {};
} else {
  cart = JSON.parse(localStorage.getItem("cart"));
}

function homepage() {
  // once item is clicked
  $(document).on("click", ".atc", function () {
    let item_id = this.id.toString();
    if (cart[item_id] != undefined) {
      quantity = cart[item_id][0] + 1;
      cart[item_id][0] = quantity;
      cart[item_id][2] =
        cart[item_id][2] +
        parseFloat(document.getElementById("price" + item_id).innerHTML);
    } else {
      quantity = 1;
      price = parseFloat(document.getElementById("price" + item_id).innerHTML);
      name = document.getElementById("nm" + item_id).innerHTML;
      cart[item_id] = [quantity, name, price];
    }
    localStorage.setItem("cart", JSON.stringify(cart));
    document.getElementById("cart").innerHTML =
      "Cart(" + Object.keys(cart).length + ")";
    location.reload();
    console.log(cart);
  });

  // run function
  displayCart(cart);

  // create items in popover menu
  function displayCart(cart) {
    cartString = "";
    cartString += "<h5>This is the cart</h5>";
    cartIndex = 1;
    for (let x in cart) {
      cartString += cartIndex;
      console.log(x);
      cartString +=
        document.getElementById("nm" + x).innerHTML +
        "Qty: " +
        cart[0] +
        "<br>";
      cartIndex += 1;
    }
    cartString += "<a href='/checkout'>Checkout</a>";
    document.getElementById("cart").setAttribute("data-content", cartString);
    $('[data-toggle="popover"]').popover();
    console.log(cart);
  }
}

// load function when doc starts
function loadFun(cart) {
  for (let x in cart) {
    document.getElementById("cart").innerHTML =
      "Cart(" + Object.keys(cart).length + ")";
  }
}

// start loading on windows start
$(window).on("load", loadFun(cart));

function check() {
  for (let item in cart) {
    let name = cart[item][1];
    let quantity = cart[item][0];

    itemString = `<li class='list-group-item'>${name}-${quantity}</li>`;
    $("#item_list").append(itemString);
  }
  $("#items").val(JSON.stringify(cart));
}
