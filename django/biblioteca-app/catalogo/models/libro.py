from django.db import models
from .categoria import Categoria
from catalogo.models.autor import Autor

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="libros")
    isbn = models.CharField(max_length=100)
    autores = models.ManyToManyField(
        Autor,
        related_name = 'libros',
        blank = True
    )
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "libro"
        verbose_name_plural = "libros"
        ordering = ["titulo"]