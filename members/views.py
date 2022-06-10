# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# def index(request):
#     return HttpResponse("Hello world!")


def index(request, id):

    products = Products.objects.all()
    print(products)
    names = [
        {'id': 1, 'name': 'Abood'},
        {'id': 2, 'name': 'Sniper'}
    ]
    for i in products:
        print(i.title)
        print(i.id)

    return render(request, 'home.html', {'names': names, 'id': id})
