from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# Modelo Categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f'Categoria #{self.id}: {self.nombre}'

# Modelo productos.
class Producto(models.Model):
    titulo = models.CharField(max_length=50, unique=True)
    imagen = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    descripcion = models.TextField(default='')
    precio = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        pass

# Modelo categorias.
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Usuario')
    cuenta = models.PositiveIntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    def __str__(self):
        pass
    
class AñadirItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    carrito = models.ForeignKey(Carrito, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        pass
