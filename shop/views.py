from django.shortcuts import render, redirect
from .models import Product
from django.core.paginator import Paginator
from shop.context_processors import requesting

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


def create_items(request, id):
    req = request.GET.get("page")

    product_objects = Product.objects.get(id=id)

    product_objects.quantity += 1
    product_objects.save()

    if req != None:
        return redirect("/")
    else:
        return redirect("/?page={}".format(requesting()))
