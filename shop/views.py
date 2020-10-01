from django.shortcuts import render, redirect
from .models import Product
from django.core.paginator import Paginator
from shop.context_processors import requesting, sect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class Index(ListView):
    model = Product
    template_name = "shop/index.html"
    paginate_by = 4

    #  search code
    def get_queryset(self):
        query = self.request.GET.get("item_name")
        #  if true return search cards
        if query:
            return Product.objects.filter(title__icontains=query)
        #  if false return all from db
        return Product.objects.all()


class Detail(DetailView):
    model = Product
    template_name = "shop/detail.html"


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
        return redirect("/")
    else:
        return redirect("/?page={}".format(requesting()))


def subtract(request, id):
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
    item, adding_prices, adding_quantities, total_price = sect(request)
    return render(
        request,
        "shop/checkout.html",
        {
            "product_objects": product_objects,
            "item": item,
            "adding_prices": adding_prices,
            "adding_quantities": adding_quantities,
            "total_column": total_price,
            "total_price": sum(total_price),
        },
    )
