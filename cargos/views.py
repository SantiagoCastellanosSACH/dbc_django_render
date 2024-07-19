from django.shortcuts import render, redirect, get_object_or_404
from .models import Cargo
from .forms import CargoForm, CargoEditForm
from django.contrib.auth.decorators import login_required

@login_required
def cargos(request):
    cargos_list = Cargo.objects.all()
    return render(request, 'cargos/cargos.html', {'cargos': cargos_list})

@login_required
def crear_cargo(request):
    if request.method == 'POST':
        form = CargoForm(request.POST) 
        if form.is_valid():
            cargo = form.save()
            return redirect('detalles_cargo', cargo_id=cargo.id)
        else:
            print("Formulario no válido. Errores:", form.errors)
    else:
        form = CargoForm()

    return render(request, 'cargos/crear_cargo.html', {'form': form})

@login_required
def detalles_cargo(request, cargo_id):
    cargo = get_object_or_404(Cargo, id=cargo_id)
    return render(request, 'cargos/cargo_detalles.html', {'cargo': cargo})

@login_required
def editar_cargo(request, cargo_id):
    cargo = get_object_or_404(Cargo, id=cargo_id)
    if request.method == 'POST':
        form = CargoEditForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('detalles_cargo', cargo_id=cargo.id)
    else:
        form = CargoEditForm(instance=cargo)

    return render(request, 'cargos/editar_cargo.html', {'form': form, 'cargo': cargo})
