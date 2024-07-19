from django.shortcuts import render, redirect, get_object_or_404
from .models import EmpresaSST
from .forms import EmpresaSSTForm, EditarEmpresaSSTForm
from django.contrib.auth.decorators import login_required

@login_required
def empresaSST(request):
    empresa_list = EmpresaSST.objects.all()
    return render(request, 'sstempresa/empresaSST.html', {'empresa': empresa_list})

@login_required
def crear_empresaSST(request):
    if request.method == 'POST':
        form = EmpresaSSTForm(request.POST, request.FILES) 
        if form.is_valid():
            empresaSST = form.save(commit=False)  # Guardar sin commit
            empresaSST.creado_por = request.user  # Asignar el usuario que creó la instancia
            empresaSST.save()  # Guardar la instancia completa
            return redirect('detalles_empresaSST', empresaSST_id=empresaSST.id)
        else:
            print("Formulario no válido. Errores:", form.errors)
    else:
        form = EmpresaSSTForm()

    return render(request, 'sstempresa/empresaSST_crear.html', {'form': form})


@login_required
def detalles_empresaSST(request, empresaSST_id):
    empresaSST = get_object_or_404(EmpresaSST, id=empresaSST_id)
    return render(request, 'sstempresa/empresaSST_detalles.html', {'empresaSST': empresaSST})

@login_required
def editar_empresaSST(request, empresaSST_id):
    empresaSST = get_object_or_404(EmpresaSST, id=empresaSST_id)
    if request.method == 'POST':
        form = EditarEmpresaSSTForm(request.POST, instance=empresaSST)
        if form.is_valid():
            form.save()
            return redirect('detalles_empresaSST', empresaSST_id=empresaSST.id)
    else:
        form = EditarEmpresaSSTForm(instance=empresaSST)

    return render(request, 'sstempresa/editar_empresaSST.html', {'form': form, 'empresaSST': empresaSST})