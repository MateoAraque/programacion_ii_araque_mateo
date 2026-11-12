from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido  = models.CharField(max_length = 100)
    nacionalidad = models.CharField(max_length = 100, blank = True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido})"
    
    class Meta:
        verbose_name_plural = "Autores"
        verbose_name = "Autor"
        ordering = ['apellido', 'nombre']
        
    