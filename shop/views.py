from django.shortcuts import render
from .models import Product, Storage
from django.core.paginator import Paginator
from .forms import StorageForm

# Create your views here.
def index(request):
    product_objects = Product.objects.all()
    storage_objects = Storage.objects.all()

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
        {
            "product_objects": product_objects,
            "storage_objects": storage_objects,
            "pro":pro,
        },
    )


def detail(request, id):
    product_object = Product.objects.get(id=id)
    return render(request, "shop/detail.html", {"product_object": product_object})


def create_items(request, id):
    form = StorageForm(request.POST or None)
    product_objects = Product.objects.get(id=id)

    if form.is_valid():
        form.save()
        return redirect("shop:index")

    return render(
        request,
        "shop/item-form.html",
        {"form": form, "product_objects": product_objects},
    )
