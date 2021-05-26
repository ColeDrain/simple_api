from django.shortcuts import render
from .models import Item
from django.http import JsonResponse

# Create your views here.
def item_list(request):
    # Create new item and save
    item = Item()
    item.save()

    # Arrange in descending order
    items = Item.objects.order_by("-timestamp")
    data = [{str(i.timestamp):str(i.id)} for i in items]
    return JsonResponse(data, safe=False)
    