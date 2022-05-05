from django.shortcuts import render

# Create your views here.


def get_firstapp(request):
    return render(request, 'firstapp/firstapp.html')
