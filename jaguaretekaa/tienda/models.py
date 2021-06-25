from django.db import models

# Create your models here.

# Modelo usuarios.


# Modelo productos.
class Producto(models.Model):
    titulo = models.CharField(max_length=50, unique=True)
    imagen = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    descripcion = models.TextField(default='')
    precio = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

# Modelo categorias.
