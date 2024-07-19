from django.db import models

class Cargo(models.Model):
    nombre_cargo = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre_cargo


