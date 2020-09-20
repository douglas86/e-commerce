from .models import Storage

def sections_processor(request):
    storage_items = Storage.objects.all()
    return {"storage_items":storage_items}
