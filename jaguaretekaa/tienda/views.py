from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from . import forms
from .models import Carrito, Categoria, Producto, ProductoAgregado


# Create your views here.
def index(request):
    # productos = Producto.objects.all()
    # productos_ordenados = productos.order_by('-fecha_creacion')
    
    # index = 0
    # productos_index = []
    
    # while index < 3:
    #     producto = productos_ordenados[index]
    #     productos_index.append(producto)
    #     index += 1
        
    # index = 3
    # productos_relacionados = []

    # while index < 10:
    #     producto = productos_ordenados[index]
    #     productos_relacionados.append(producto)
    #     index += 1
        
    # data = {
    #     'productos_index': productos_index,
    #     'productos_relacionados': productos_relacionados,
    # }
    
    return render(request, 'index.html', )
    
def about(request):
    return render(request, 'about.html', {})


def home(request):
    return render(request, 'home.html', {})

def resultado(request):
    return render(request, 'resultado.html', {})
def producto(request):
    return render(request, 'producto.html', {})

def acceder(request):
    return render(request, 'templates/acceder.html', {})

def cuentas(request):
    return(request, 'templates/cuentas.html', {})


def contact(request):
    pass

def signin(request):
    pass

def signup(request):
    pass

def products(request):
    pass

def product(request):
    pass

def add_product(request):
    pass

def edit_product(request):
    pass

def delete_product(request):
    pass

def categories(request):
    pass

def add_category(request):
    pass

def edit_category(request):
    pass

def delete_category(request):
    pass

def result(request):
    pass

def cart(request):
    pass

def cart_prod_add(request):
    pass

def cart_prod_edit(request):
    pass

def void(request):
    pass
