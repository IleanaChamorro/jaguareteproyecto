
from django.db.models import Q

from .models import Categoria, Producto


def search(busqueda):
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(
        Q(titulo__icontains = busqueda) |
        Q(descripcion__icontains = busqueda)
    ).distinct()

    data = {
        'productos': productos,
        'categorias': categorias
    }

    return data
