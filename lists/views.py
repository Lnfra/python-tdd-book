from django.http import HttpResponse
from django.shortcuts import render

from lists.models import Item


def home_page(request):
    if request.method == "POST":
        item = Item.objects.create(text=request.POST['item_text'])
        return render(request, 'home.html', {'new_item_text': item.text,})
    else:
        return render(request, 'home.html')