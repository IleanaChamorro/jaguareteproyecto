from django.http import HttpResponse
from django.shortcuts import render

from .models import AñadirItem, Carrito, Categoria, Producto


# Create your views here.
def index(request):
    sesion = request.session
    return render(request, 'templates/index.html', {
        'sesion': sesion
    })
def menu(request):
    return render(request, 'menu.html')
def about(request):
    return render(request, 'about.html')
def footer(request):
    return render(request, 'footer.html')
