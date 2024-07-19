from django.contrib import admin
from .models import Contrato

class ContratoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de objetos de Contratos
    list_display = ('tipo_contrato', 'cargo_contrato', 'fecha_inicio', 'fecha_terminacion')

    # Campos por los que se puede buscar en la lista de objetos de Contratos
    search_fields = ('tipo_contrato', 'cargo_contrato', 'nombre_empleado', 'correo_empleado')

    # Campos por los que se pueden filtrar los objetos de Contratos
    list_filter = ('tipo_contrato', 'cargo_contrato', 'fecha_inicio', 'fecha_terminacion')

# Registra el modelo Contratos en el administrador utilizando ContratosAdmin
admin.site.register(Contrato, ContratoAdmin)
