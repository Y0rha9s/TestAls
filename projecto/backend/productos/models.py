from django.db import models
from django.utils import timezone

class Producto(models.Model):
    nombre = models.CharField(
        max_length=200, 
        verbose_name="Nombre del Producto",
        help_text="Nombre descriptivo del producto"
    )
    fecha = models.DateTimeField(
        default=timezone.now, 
        verbose_name="Fecha de Creación",
        help_text="Fecha y hora de creación del producto"
    )
    valor = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Valor",
        help_text="Precio del producto en pesos chilenos"
    )
    imagen = models.ImageField(
        upload_to='productos/', 
        null=True, 
        blank=True, 
        verbose_name="Imagen del Producto",
        help_text="Imagen representativa del producto"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.nombre} - ${self.valor}"

    def get_image_url(self):
        if self.imagen:
            return self.imagen.url
        return None