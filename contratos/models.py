from django.db import models
from personas.models import Persona
from cargos.models import Cargo
from django.utils import timezone
import locale
from datetime import datetime

class Contrato(models.Model):
    razón_social = models.CharField(max_length=255, verbose_name='Razón social', default='DIGITAL BRIDGE COMMUNICATIONS')
    nit_empresa = models.CharField(max_length=20, default='901481430-5')
    nombre_representante_legal = models.CharField(max_length=255, default='Jonathan Cifuentes Cadena')
    cargo_representante_legal = models.CharField(max_length=255, default='Gerente')
    tipo_doc_representante_legal = models.CharField(max_length=20, verbose_name='Tipo doc representante legal', default='CC')
    numero_doc_representante_legal = models.CharField(max_length=20, verbose_name='Número doc representante legal', default='1016019519')
    lugar_expedicion_doc_representante_legal = models.CharField(max_length=255, verbose_name='Lugar expedición doc representante legal', default='Bogotá')
    celular_representante_legal = models.CharField(max_length=20, default='+57 320 8434390')
    correo_representante_legal = models.EmailField(max_length=255, verbose_name='Correo electrónico representante legal', default='jcifuentes@dbcw.com.co')
    ubicacion = models.CharField(max_length=255, verbose_name='Ubicación', default='Jenesano-Boyacá')
    direccion_notificacion_judicial= models.CharField(max_length=255, verbose_name='Dirección de notificación judicial', default='Calle 8 #3-42')

    empleado = models.ForeignKey(Persona, on_delete=models.CASCADE)

    TIPO_CONTRATO_CHOICES = [
        ('Contrato de Trabajo a Tiempo Completo - Término Fijo', 'Contrato de Trabajo a Tiempo Completo - Término Fijo'),
        ('Contrato de Trabajo a Tiempo Parcial - Término Fijo', 'Contrato de Trabajo a Tiempo Parcial - Término Fijo'),
        ('Contrato de Aprendizaje', 'Contrato de Aprendizaje'),
    ]
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Terminado', 'Terminado'),
        ('Vencido', 'Vencido'),
        ('Por vencer', 'Por vencer'),
        ('Liquidado', 'Liquidado'),
    ]
    cargo_contrato = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    tipo_contrato = models.CharField(max_length=255, choices=TIPO_CONTRATO_CHOICES)
    salario = models.DecimalField(max_digits=10, decimal_places=0) 

    def formato_salario(self):
        locale.setlocale(locale.LC_ALL, '')
        salario_formateado = locale.currency(self.salario, grouping=True)
        return salario_formateado

    duracion_contrato = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_terminacion = models.DateField()
    fecha_pre_aviso = models.DateField()
    estado = models.CharField(max_length=100, choices=ESTADO_CHOICES, default='Activo')
    fecha_creacion_contrato = models.DateField(auto_now_add=True)  
    adjunto_contrato = models.FileField(upload_to='adjuntos_contratos/')
    fecha_carga_adjunto_contrato = models.DateField(auto_now_add=True)
    adjunto_preaviso = models.FileField(upload_to='adjuntos_preaviso/')
    dias_restantes = models.PositiveIntegerField(default=0, editable=False)
    consecutivo = models.PositiveIntegerField(unique=True, blank=True, null=True)

    def calcular_dias_restantes(self):
        hoy = datetime.now().date()
        dias_restantes = (self.fecha_terminacion - hoy).days
        return dias_restantes

    def actualizar_estado(self, save_instance=True):
        dias_restantes = self.calcular_dias_restantes()
        if dias_restantes < 0:
            nuevo_estado = 'Vencido'
        elif dias_restantes < 20:
            nuevo_estado = 'Por vencer'
        else:
            nuevo_estado = self.estado
        
        if self.estado != nuevo_estado:
            self.estado = nuevo_estado
            if save_instance:
                self.save(update_fields=['estado'])

    def save(self, *args, **kwargs):
        if self.consecutivo is None:
            ultimo_consecutivo = Contrato.objects.aggregate(models.Max('consecutivo'))['consecutivo__max']
            if ultimo_consecutivo is None:
                self.consecutivo = 140
            else:
                self.consecutivo = ultimo_consecutivo + 1
        self.actualizar_estado(save_instance=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tipo_contrato} - Salario: ${self.salario:,.0f}"
