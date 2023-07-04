from django.db import models
from django.utils import timezone


class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")

    class Meta:
        verbose_name = "categoría de productos"
        verbose_name_plural = "categorías de productos"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    OPCIONES_MONEDA = [
        ("ARS", '1 - ARS'),
        ("USD", '2 - USD'),
    ]
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="categoría")
    stock = models.FloatField()
    moneda = models.CharField(choices=OPCIONES_MONEDA, max_length=3, default="ARS")
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    precio_costo = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=250, blank=True, null=True, verbose_name="descripción")
    fecha_actualizacion = models.DateTimeField(default=timezone.now, editable=False, verbose_name="fecha de actualización")
    imagen = models.ImageField(upload_to="productos", blank=True, null=True)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return f"{self.nombre} - {self.stock} - {self.fecha_actualizacion}"
    
    