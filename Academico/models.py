from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre= models.CharField(max_length=60)
    credito = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} (Creditos: {1})"
        return texto.format(self.nombre , self.credito)
