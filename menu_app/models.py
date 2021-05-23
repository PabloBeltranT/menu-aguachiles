from django.db import models

# Create your models here.
class Productos(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.CharField(max_length=5)
    estado = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='aguachiles', null=True)
    def __str__(self):
        return self.titulo