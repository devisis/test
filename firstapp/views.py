from django.shortcuts import render, redirect
from .models import Item
# Create your views here.


def get_first_app(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'firstapp/firstapp.html', context)


def add_item(request):
    if request.method == "POST":
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)
        
        return redirect('get_first_app')
    return render(request, 'firstapp/add_item.html')
