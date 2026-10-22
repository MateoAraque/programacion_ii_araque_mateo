from django.db import models

# Create your models here.
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cementerio(models.Model):
    nombre = models.CharField(max_length=100)
    parcela = models.TextField(blank=True)
    fecha_muerte = models.DateTimeField(blank=True)
    hora_muerte = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre