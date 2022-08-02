from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Historias(models.Model):
    titulo= models.CharField(max_length=300)
    subtitulo= models.CharField(max_length=400)
    cuerpo= models.CharField(max_length=800)
    autor= models.CharField(max_length=100)
    fecha= models.CharField(max_length=50)

    def __str__(self):
        return f"Titulo: {self.titulo}"

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta avatares media
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
