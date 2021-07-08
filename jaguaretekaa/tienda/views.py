from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, User
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone

from . import forms
from .forms import CustomUserCreationForm, ProductoForm
from .models import Carrito, Categoria, Producto, ProductoAgregado
from .search import search

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
    busqueda = request.GET.get("buscar")
    categorias = Categoria.objects.all()
    prod = get_object_or_404(Producto, id=id)

    if busqueda:
        data = search(busqueda)
    else:

        data = {
            'producto': prod,
            'categorias': categorias
        }

    return render(request, 'producto.html', data)

@permission_required('tienda.add_product')
def add_product(request, id):
    
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
            
    return render(request, 'nuevo_producto.html', data)
            
@permission_required('tienda.edit_product')
def edit_product(request, id):
    prod = get_object_or_404(Producto, id=id)

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

    return render(request, 'producto_actualizado.html', data)

def delete_product(request, id):
    prod = get_object_or_404(Producto, id=id)
    prod.delete()
    return redirect(to="")

def categories(request):
    pass

def add_category(request):
    pass

def edit_category(request, id):
    pass

def delete_category(request, id):
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
    cart = Carrito.objects.filter(usuario=request.user.id).first()
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()

    if cart:
        prod_cart = cart.productos.all()       
        mensaje = ""
        data = {
            'cart': cart,
            'cart_prod': prod_cart,
            'productos': productos,
            'categorias': categorias,
            'mensaje': mensaje
        }
    else:
        mensaje = "No hay productos en el carrito"
        data = {
            'cart': cart,
            'mensaje': mensaje,
            'productos': productos,
            'categorias': categorias
        }
    
    return render(request, 'carrito.html', data)

@login_required
def cart_prod_add(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto_agregado = ProductoAgregado.objects.get_or_create(
        producto = producto,
        usuario = request.user,
        agregado = False
    )

    producto_existente_carrito = Carrito.objects.filter(usuario=request.user, ya_pedido=False)

    if producto_existente_carrito.exists():
        agrega_producto = producto_existente_carrito[0]

        if agrega_producto.productos.filter(producto__id=id).exists():
            producto_agregado.cantidad += 1
            producto_agregado.save()
            messages.info(request, "Agregada/s unidad/es")
            return redirect("tienda:cart")
    else:
        fecha_pedido = timezone.now()
        agregado_al_pedido = Carrito.objects.create(usuario=request.user, fecha=fecha_pedido)
        agregado_al_pedido.productos.add(producto_agregado)
        messages.info(request, "Producto agregado al carrito")
        return redirect("tienda:cart")
    return redirect("tienda:cart")

def cart_prod_edit(request):
    user_cart = Carrito.objects.filter(usuario=request.user.id).first()
    productos = Producto.objects.get(id=id)

    if user_cart:
        if not productos in user_cart.productos.all():
            user_cart.productos.add(productos)
        else:
            user_cart.productos.remove(productos)

        new_total = 0

        for item in user_cart.productos.all():
            new_total += item.precio

        user_cart.total = new_total
        user_cart.save()
    else:
        new_cart = Carrito()
        new_cart.usuario = request.user
        new_cart.save()
        

        if not productos in new_cart.productos.all():
            new_cart.productos.add(productos)
        else:
            new_cart.productos.remove(productos)

        new_total = 0

        for item in new_cart.productos.all():
            new_total += item.precio

        new_cart.total = new_total
        new_cart.save()

def void(request):
    cart = Carrito.objects.filter(usuario=request.user.id).first()

    for p in cart.productos.all():
        cart.productos.remove(p)

    cart.total = 0
    cart.save()

    return redirect(to="tienda:cart")
