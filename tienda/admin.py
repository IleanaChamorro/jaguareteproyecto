from django.contrib import admin

from .models import AñadirItem, Carrito, Categoria, Producto

# Register your models here.
admin.site.register(AñadirItem)
admin.site.register(Carrito)
admin.site.register(Categoria)
admin.site.register(Producto)
