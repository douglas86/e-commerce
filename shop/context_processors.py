from .models import Product


def sections_processor(request):
    products = Product.objects.all()
    return {"products": products}
