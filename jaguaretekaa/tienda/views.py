from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from . import forms
from .forms import CustomUserCreationForm, ProductoForm
from .models import Carrito, Categoria, Producto, ProductoAgregado

# Create your views here.

def index(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    productos_ordenados = productos.order_by('-fecha_creacion')
    
    index = 0
    productos_index = []
    
    print(len(productos))
    
    while index < 3:
        producto = productos_ordenados[index]
        productos_index.append(producto)
        index += 1
        
    index = 3
    productos_relacionados = []

    while index < 7:
        producto = productos_ordenados[index]
        productos_relacionados.append(producto)
        index += 1
        
    
    return render(request, 'index.html', {'productos_index': productos_index, 'productos': productos})
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    pass

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "El usuario ha sido creado correctamente")
            return redirect(to="")
    return render(request, 'registration/register.html', data)

def logout(request):
    pass

def product(request,id):
    pass

@permission_required('core.add_product')
def add_product(request):
    
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto agregado"
        else:
            data["form"] = formulario
@permission_required('core.edit_product')
def edit_product(request):
    prod = get_object_or_404(producto, id=id)

    data = {
        'form': ProductoForm(instance=prod)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=prod, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="")
        else:
            data["form"] = formulario

    return render(request, 'core/producto/modificar.html', data)

def delete_product(request):
    prod = get_object_or_404(producto, id=id)
    prod.delete()
    return redirect(to="")

def categories(request):
    pass

def add_category(request):
    pass

def edit_category(request):
    pass

def delete_category(request):
    pass

def result(request):
    query = request.GET.get('q')
    if query:
        queryset_productos = Producto.objects.filter(
            Q(titulo__icontains=query) | Q(categoria__descripcion__icontains=query)
        )
        queryset_categorias = Categoria.objects.filter(
            Q(descripcion__icontains=query)
        )
    else:    
        queryset_productos = Producto.objects.all()
        queryset_categorias = Categoria.objects.all()
        
    return render(request, 'resultado.html', {"queryset_productos": queryset_productos, "queryset_categorias": queryset_categorias})

def cart(request):
    pass

def cart_prod_add(request):
    pass

def cart_prod_edit(request):
    pass

def void(request):
    pass
