from django.shortcuts import render, redirect, get_object_or_404
from .models import Contrato
from .forms import ContratoForm, ContratoEditForm
from django.contrib.auth.decorators import login_required

@login_required
def contrato(request):
    contratos_list = Contrato.objects.all()
    return render(request, 'contratos/contratos.html', {'contratos': contratos_list})

@login_required
def crear_contrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST, request.FILES) 
        if form.is_valid():
            contrato = form.save()
            return redirect('detalles_contrato', contrato_id=contrato.id)
        else:
            print("Formulario no válido. Errores:", form.errors)
    else:
        form = ContratoForm()

    return render(request, 'contratos/crear_contrato.html', {'form': form})

@login_required
def detalles_contrato(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    return render(request, 'contratos/contratoDetalles.html', {'contrato': contrato})

@login_required
def editar_contrato(request, id):
    contrato = Contrato.objects.get(id=id)
    if request.method == 'POST':
        form = ContratoEditForm(request.POST, request.FILES, instance=contrato)
        if form.is_valid():
            form.save()
            return redirect('detalles_contrato', contrato_id=contrato.id)
    else:
        form = ContratoEditForm(instance=contrato)
    return render(request, 'contratos/editar_contrato.html', {'form': form, 'contrato': contrato})