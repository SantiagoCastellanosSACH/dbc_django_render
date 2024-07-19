from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from personas.models import Persona


TIPOS_DOCUMENTO_CHOICES = [
    ('Perfil sociodemográfico', 'Perfil sociodemográfico'),
    ('Análisis de puesto de trabajo', 'Análisis de puesto de trabajo'),
    ('Exámenes médicos', 'Exámenes médicos'),
    ('Otros', 'Otros'),
]

class PersonasSST(models.Model):
    persona_SST = models.ForeignKey(Persona, on_delete=models.CASCADE)

    tipo_documento = models.CharField(max_length=50, choices=TIPOS_DOCUMENTO_CHOICES, verbose_name='Tipo de Documento')
    nombre_documento = models.CharField(max_length=255, verbose_name='Nombre del Documento')
    archivo = models.FileField(upload_to='adjuntos_personaSST/')
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creado por')
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Creación')

    def __str__(self):
        return self.nombre_persona
