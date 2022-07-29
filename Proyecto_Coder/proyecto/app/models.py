from django.db import models

# Create your models here.

class Historias(models.Model):
    titulo= models.CharField(max_length=300)
    subtitulo= models.CharField(max_length=400)
    cuerpo= models.CharField(max_length=800)
    autor= models.CharField(max_length=100)
    fecha= models.CharField(max_length=50)