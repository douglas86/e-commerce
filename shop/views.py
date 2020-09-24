from django.shortcuts import render, redirect
from .models import Product, Storage
from django.core.paginator import Paginator
from .forms import StorageForm

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
    product_objects = Product.objects.get(id=id)
    storage_objects = Storage.objects.create(
        title="%s" % product_objects.title,
        price="%s" % product_objects.price,
        quantity="1",
    )

    storage_objects

    return redirect("/")
