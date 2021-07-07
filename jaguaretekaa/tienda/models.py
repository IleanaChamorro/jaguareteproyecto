from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Categoria(models.Model):
    descripcion = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.descripcion

class Producto(models.Model):
    class Meta:
        permissions = (("can_add_productos", "Can add productos"),)
        
    titulo = models.CharField(max_length=50, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='uploaded_images')
    descripcion = models.TextField(default='')
    precio = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo

    def id(self):
        return reverse("tienda:producto", kwargs={'pk': self.pk})
        
    def agregar_carrito(self):
        return reverse('tienda: agregar_carrito', kwargs={'pk': self.pk})

    def sacar_carrito(self):
        return reverse('tienda:sacar_carrito', kwargs={'pk': self.pk})
    
    def mostrar_imagen(self):
        with open(self.imagen.path) as fp:
            return fp.read().replace('\n', '<br>')

class ProductoAgregado(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    agregado = models.BooleanField(default=False)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=1)
    
    def __str__(self):
        return f'{self.cantidad} of {self.producto.titulo}'
    
    def precio_total_producto(self):
        return self.cantidad * self.producto.precio

class Carrito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Usuario')
    productos = models.ManyToManyField(ProductoAgregado)
    fecha = models.DateTimeField(auto_now_add=True)
    ya_pedido = models.BooleanField(default=False)
    
    def __str__(self):
        return self.usuario.username
    
    def precio_total_carrito(self):
        total = 0
        for producto in self.productos.all():
            total += producto.precio_total_producto()
        return total

class Cliente(models.Model):
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Orden
# class Order(models.Model):
    # cliente = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    # fecha_pedido = models.DateTimeField(auto_now_add=True)
    # completado = models.BooleanField(default=False, null=True, blank=False)
    # id_transaccion = models.CharField(max_length=200, null=True)
    
    # def __str__(self):
    #     return str(self.id)
