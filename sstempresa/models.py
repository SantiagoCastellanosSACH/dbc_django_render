from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

TIPOS_DOCUMENTO_CHOICES = [
    ('Capacitaciones', 'Capacitaciones'),
    ('Comité COPASST', 'Comité COPASST'),
    ('Comité Convivencia', 'Comité Convivencia'),
    ('Otros', 'Otros'),
]

class EmpresaSST(models.Model):
    nombre_documento = models.CharField(max_length=255, verbose_name='Nombre Documento')
    tipo_documento = models.CharField(max_length=50, choices=TIPOS_DOCUMENTO_CHOICES, verbose_name='Tipo de Documento')
    archivo = models.FileField(upload_to='adjuntos_empresaSST/')
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creado por')
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Creación')

    def __str__(self):
        return self.nombre_documento