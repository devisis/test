from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
# Create your views here.


def get_first_app(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'firstapp/firstapp.html', context)


def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_first_app')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'firstapp/add_item.html', context)


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    form = ItemForm(instance=item)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_first_app')
    context = {
        'form': form
    }
    return render(request, 'firstapp/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_first_app')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_first_app')
