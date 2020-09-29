from django.shortcuts import render, redirect
from .models import Product
from django.core.paginator import Paginator
from shop.context_processors import requesting, sect

# Create your views here.
def index(request):
    product_objects = Product.objects.all()

    #  search code
    item_name = request.GET.get("item_name")
    if item_name != "" and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    #  paginator code
    paginator = Paginator(product_objects, 4)
    page = request.GET.get("page")
    product_objects = paginator.get_page(page)

    return render(
        request,
        "shop/index.html",
        {"product_objects": product_objects},
    )


def detail(request, id):
    product_object = Product.objects.get(id=id)
    return render(request, "shop/detail.html", {"product_object": product_object})


#  add to cart view
def create_items(request, id):
    #  looks to see what page you are on
    req = request.GET.get("page")

    #  grabs item from db by id number
    product_objects = Product.objects.get(id=id)

    #  adds one to quantity then saves to db
    product_objects.quantity += 1
    product_objects.save()

    requestig = request.get_full_path()

    #  makes sure to stay on current page
    if req != None:
        return redirect("/{}".format(your_domain))
    else:
        return redirect("/?page={}".format(requesting()))


def subtract(request, id):
    #  looks to see what page you are on
    req = request.GET.get("page")

    #  grabs item from db by id number
    product_objects = Product.objects.get(id=id)

    #  adds one to quantity then saves to db
    product_objects.quantity -= 1
    product_objects.save()

    return redirect("/checkout")

    #  makes sure to stay on current page
    #  if req != None:
    #      return redirect("/")
    #  else:
    #      return redirect("/?page={}".format(requesting()))


def checkout(request):
    product_objects = Product.objects.all()
    item, adding_prices, adding_quantities = sect(request)
    return render(
        request,
        "shop/checkout.html",
        {
            "product_objects": product_objects,
            "item": item,
            "adding_prices": adding_prices,
            "adding_quantities": adding_quantities,
        },
    )
