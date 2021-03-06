from django.shortcuts import render, redirect

from lists.models import Item


def home_page(request):
    if request.method == "POST":
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    else:
        return render(request, 'home.html', {'items': Item.objects.all()})
