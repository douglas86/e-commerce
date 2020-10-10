from django.shortcuts import render, redirect
from .models import Product
from django.core.paginator import Paginator
from shop.context_processors import requesting, sect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import F
from django.urls import reverse_lazy


class Index(ListView):
    model = Product
    template_name = "shop/index.html"
    paginate_by = 4  # sets the amount of items to display on page

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


#  updates quantity in database
class Update(DetailView):
    model = Product
    template_name = "shop/update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #  takes the dictionary and draws out second value in dict
        valued_item = list(self.kwargs.values())[1]
        #  URL_path = list(self.kwargs.values())[2]
        #  checks value of valued_item
        if valued_item == 2:
            #  subtract 1 from db
            if self.object.quantity > 0:
                self.object.quantity = F('quantity') - 1
        else:
            #  adds 1 to db
            self.object.quantity = F('quantity') + self.kwargs['number']
        #  save to db
        self.object.save()
        #  print(self.kwargs['next'])
        context['next'] = self.request.GET.get('request.get_full_path', None)
        print(context)
        return context

    def get_seccess_url(self):
        path = request.GET.get('next', None)
        print(request.GET.get('param1', None))
        return redirect(path)

    #  def get_success_url(self):
    #      URL_path = self.kwargs['next']
    #      print(URL_path)
    #      print(request.GET.get('next'))
    #      return redirect(request.GET.get('next'))



    #  def dispatch(self):
    #      return redirect(URL_path)



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
