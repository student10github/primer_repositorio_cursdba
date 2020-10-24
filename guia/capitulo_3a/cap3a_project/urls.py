"""cap3a_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cap3a_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_page_view, name='home'),
    path('carbonara/', views.carbonara_page_view, name='carbonara'),
    path('menu_infantil/', views.menu_infantil_page_view, name='menu_infantil'),
    path('receta_facil/', views.receta_facil_page_view, name='receta_facil'),
    path('mafe/', views.mafe_page_view, name='mafe'),
    path('feijoada/', views.feijoada_page_view, name='feijoada'),
    path('pizza/', views.pizza_page_view, name='pizza'),
    path('canelones/', views.canelones_page_view, name='canelones'),
    path('flor_de_calabacin/', views.flor_de_calabacin_page_view, name='flor_de_calabacin'),
    path('gazpacho/', views.gazpacho_page_view, name='gazpacho'),
    path('sopa_de_noodles/', views.sopa_de_noodles_page_view, name='sopa_de_noodles'),
    path('ensaladilla_rusa/', views.ensaladilla_rusa_page_view, name='ensaladilla_rusa'),

]