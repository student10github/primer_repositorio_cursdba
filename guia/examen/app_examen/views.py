from django.shortcuts import render

# Create your views here.
def examen_page_view(request):
    parametros = {'nota': 10}
    return render(request, 'examen.html', parametros)

def django_page_view(request):
    return render(request, 'django.html')

