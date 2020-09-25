from .models import Product

#  create a list that append what query you are on
#  from the url path
req = []

def sections_processor(request):

    #  append the number at the end of the page
    #  /?page=1 number to append
    req.clear() # clears list before appending
    req.append(request.GET.get("page"))

    #  takes the values id and quantity out of the db
    pro = Product.objects.values("id", "quantity")
    length = len(pro)
    lists = []

    #  iterates over all quantities to check if it is
    #  greater than 0
    for i in range(length):
        p = pro[i].values()
        l = list(p)[1]
        if l > 0:
            lists.append(l)

    le = len(lists)

    return {"le": le, "req":req}

def requesting():
    return req.pop()
