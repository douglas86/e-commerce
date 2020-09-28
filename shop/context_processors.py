from .models import Product

#  create a list that append what query you are on
#  from the url path
req = [] # this is to get the reference number of the page that you are on
amounts = []
titles = []

item = {}
attributes = Product.objects.values("id", "title", "price", "quantity")
length = len(attributes)


def sect(request):
    req.clear()
    req.append(request.GET.get("page"))
    amounts.clear()
    titles.clear()

    l = len(list(attributes[0].keys()))

    for i in range(length):
        val = list(attributes[i].values())
        ids = val[0]
        title = val[1]
        price = val[2]
        quant = val[3]
        if quant > 0:
            item["stock{}".format(i+1)] = ids, title, price, quant


    #  for i in range(l):
    #      everything.append(list(item.values())[i])

    return item
    

def sections_processor(request):

    #  append the number at the end of the page
    #  /?page=1 number to append
    req.clear() # clears list before appending
    req.append(request.GET.get("page"))

    #  takes the values id and quantity out of the db
    pro = Product.objects.values("id", "quantity", "title")
    length = len(pro)
    lists = []
    titles = []

    #  iterates over all quantities to check if it is
    #  greater than 0
    for i in range(length):
        p = pro[i].values()
        l = list(p)[1]
        t = list(p)[2]
        if l > 0:
            lists.append(l)
            titles.append(t)

    #  returns the length of the list
    #  for add to cart in navbar
    le = len(lists)

    zippedList = zip(lists, titles)


    return {"le": le, "zippedList":zippedList}

def requesting():
    return req.pop()
