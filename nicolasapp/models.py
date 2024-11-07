from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Platos(models.Model):
    nombre_plato = models.CharField(max_length=12, unique=True)
    precio = models.CharField(max_length=100)
    ingredientes = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_plato
