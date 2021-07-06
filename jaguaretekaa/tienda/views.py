from django.http import HttpResponse
from django.shortcuts import render

from .models import AñadirItem, Carrito, Producto


# Create your views here.
def index(request):
    sesion = request.session
    return render(request, 'templates/index.html', {
        'sesion': sesion
    })

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
