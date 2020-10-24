from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request, 'home.html')

def carbonara_page_view(request):
    return render(request, 'carbonara.html')

def menu_infantil_page_view(request):
    return render(request, 'menu_infantil.html')

def receta_facil_page_view(request):
    return render(request, 'receta_facil.html')

def mafe_page_view(request):
    return render(request, 'mafe.html')

def feijoada_page_view(request):
    return render(request, 'feijoada.html')

def pizza_page_view(request):
    return render(request, 'pizza.html')

def canelones_page_view(request):
    return render(request, 'canelones.html')

def flor_de_calabacin_page_view(request):
    return render(request, 'flor_de_calabacin.html')

def gazpacho_page_view(request):
    return render(request, 'gazpacho.html')

def sopa_de_noodles_page_view(request):
    return render(request, 'sopa_de_noodles.html')

def ensaladilla_rusa_page_view(request):
    return render(request, 'ensaladilla_rusa.html')