# main/views.py
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.db.models import Count
from django.utils import timezone
from personas.models import Persona
from sstpersonas.models import PersonasSST
from contratos.models import Contrato
import datetime
from django.shortcuts import render
from django.db.models.functions import ExtractMonth
from django.utils import timezone
from datetime import timedelta
import calendar

@login_required
def mostrar_perfil(request):
    usuario = request.user
    context = {
        'usuario': usuario
    }
    return render(request, 'perfil/perfil.html', context)

def recuperar_contrasena(request):
    return render(request, 'registration/olvide-contraseña.html')

def logout_usuario(request):
    logout(request)
    return redirect('login')


@login_required
def principal(request):
    # Conteo de personas
    total_personas = Persona.objects.count()

    # Conteo de contratos
    total_contratos = Contrato.objects.count()

    # Conteo de archivos adjuntos de personas SST
    total_archivos_adjuntos = PersonasSST.objects.count()

    # Obtener datos para el gráfico de contrataciones promedio por fechas
    contratos_por_mes = Contrato.objects \
        .annotate(mes_creacion=ExtractMonth('fecha_creacion_contrato')) \
        .values('mes_creacion') \
        .annotate(total=Count('id'))

    # Convertir los números de mes a nombres de mes
    for mes_data in contratos_por_mes:
        mes_num = mes_data['mes_creacion']
        mes_nombre = calendar.month_name[mes_num]
        mes_data['mes_nombre'] = mes_nombre

    # Contratos a punto de vencer
    contratos_a_punto_de_vencer = Contrato.objects.filter(fecha_terminacion__gte=timezone.now(), fecha_terminacion__lte=timezone.now() + timedelta(days=30)).count()

    context = {
        'total_personas': total_personas,
        'total_contratos': total_contratos,
        'total_archivos_adjuntos': total_archivos_adjuntos,
        'contratos_por_mes': contratos_por_mes,
        'contratos_a_punto_de_vencer': contratos_a_punto_de_vencer,
    }

    return render(request, 'Principal.html', context)
    