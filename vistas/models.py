from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fecha(models.Model):
    fecha = models.DateTimeField()

class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

class Dispensar(models.Model):
    hora = models.IntegerField()
    minuto = models.IntegerField()
    id_usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)