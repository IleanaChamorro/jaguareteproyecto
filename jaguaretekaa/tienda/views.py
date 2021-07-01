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

def acceder(request):
    return render(request, 'templates/acceder.html', {})

def cuentas(request):
    return(request, 'templates/cuentas.html', {})