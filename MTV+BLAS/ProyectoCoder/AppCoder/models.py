from django.db import models

# Create your models here.
class Familia(models.Model):
    
    nombre = models.CharField(max_length=80)
    relacion = models.CharField(max_length=80)
    nacimiento = models.CharField(max_length=80)
    edad = models.IntegerField()
