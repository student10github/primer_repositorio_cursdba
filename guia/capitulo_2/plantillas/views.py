from django.shortcuts import render
from django.http import HttpResponse
from random import randrange, randint, random

# Create your views here.

def numero_aleatorio():
    numero_aleatorio = randrange(100)
    return numero_aleatorio

def home_page_view(request):
    return render(request, 'home.html')

"""
def about_page_view(request):
    parametros = {'numero_favorito': 77}
    return render(request, 'about.html', parametros)
"""

def about_page_view(request):
    num_aleatorio = numero_aleatorio()
    parametros = {'numero_favorito': num_aleatorio}
    return render(request, 'about.html', parametros)


def test_page_view(request):
    return render(request, 'test.html')


