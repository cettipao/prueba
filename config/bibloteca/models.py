from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length = 20)

class Libro(models.Model):
    titulo = models.CharField(max_length = 20)
    editorial = models.CharField(max_length = 20)
    paginas = models.IntegerField()
    autor = models.ForeignKey(
        'Autor',
        on_delete=models.CASCADE,
        null = False,
    )

