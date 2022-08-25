from django.db import models

# Create your models here.
class Contactos(models.Model):
    foto = models.ImageField(upload_to='static/uploads/fotos',)
    nombre = models.CharField(max_length=40, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return str(self.nombre)