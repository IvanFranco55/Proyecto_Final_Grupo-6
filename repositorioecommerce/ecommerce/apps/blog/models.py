from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=60)
    descripcion = models.TextField(null = True, blank=True)

    def __str__(self):
        return self.nombre_categoria

class Articulo(models.Model):
    titulo = models.CharField(max_length=60)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='articulos/',max_length=255, null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name="comentarios")

    def __str__(self):
        return f"Comentario de: {self.autor.username}"