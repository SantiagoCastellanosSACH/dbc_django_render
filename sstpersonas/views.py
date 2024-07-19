from django.shortcuts import render, redirect, get_object_or_404
from .models import PersonasSST
from .forms import PersonasSSTForm, EditarPersonasSSTForm
from django.contrib.auth.decorators import login_required

@login_required
def personasSST(request):
    personasSST = PersonasSST.objects.all()
    return render(request, 'sstpersonas/personasSST.html', {'personasSST': personasSST})

@login_required
def adjuntar_personaSST(request):
    if request.method == 'POST':
        form = PersonasSSTForm(request.POST, request.FILES) 
        if form.is_valid():
            personaSST = form.save(commit=False)
            personaSST.creado_por = request.user
            personaSST.save()
            return redirect('detalles_personaSST', personaSST_id=personaSST.id)
        else:
            print("Formulario no válido. Errores:", form.errors)
    else:
        form = PersonasSSTForm()

    return render(request, 'sstpersonas/personasSST_crear.html', {'form': form})


@login_required
def detalles_personaSST(request, personaSST_id):
    personaSST = get_object_or_404(PersonasSST, id=personaSST_id)
    return render(request, 'sstpersonas/personasSST_detalles.html', {'personaSST': personaSST})


@login_required
def editar_personaSST(request, personaSST_id):
    personaSST = get_object_or_404(PersonasSST, id=personaSST_id)
    if request.method == 'POST':
        form = EditarPersonasSSTForm(request.POST, instance=personaSST)
        if form.is_valid():
            form.save()
            return redirect('detalles_personaSST', personaSST_id=personaSST.id)
    else:
        form = EditarPersonasSSTForm(instance=personaSST)

    return render(request, 'sstpersonas/personasSST_editar.html', {'form': form, 'personaSST': personaSST})
