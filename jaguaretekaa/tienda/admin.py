from django.contrib import admin

from .models import Carrito, Categoria, Cliente, Producto, ProductoAgregado

admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(ProductoAgregado)
admin.site.register(Categoria)
admin.site.register(Cliente)
