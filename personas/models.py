from django.db import models

class Persona(models.Model):
    nombre_persona = models.CharField(max_length=255)
    TIPO_DOCUMENTO_CHOICES = [
        ("CC", "Cédula de Ciudadanía"),
        ("CE", "Cédula de Extranjería"),
        ("P", "Pasaporte"),
    ]
    tipo_documento_persona = models.CharField(
        max_length=2, choices=TIPO_DOCUMENTO_CHOICES
    )
    numero_documento_persona = models.CharField(max_length=20)
    correo_persona = models.EmailField()
    celular_persona = models.CharField(max_length=20)
    direccion_residencia_persona = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_persona  


