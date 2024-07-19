from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona
from .forms import PersonaForm, PersonaEditForm
from django.contrib.auth.decorators import login_required

@login_required
def personas(request):
    personas_list = Persona.objects.all()
    return render(request, 'personas/personas.html', {'personas': personas_list})

@login_required
def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = form.save()
            return redirect('detalles_persona', persona_id=persona.id)
    else:
        form = PersonaForm()
    
    return render(request, 'personas/crear_persona.html', {'form': form})

@login_required
def detalles_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)
    return render(request, 'personas/personaDetalles.html', {'persona': persona})

@login_required
def editar_persona(request, id):
    persona = Persona.objects.get(id=id)
    if request.method == 'POST':
        form = PersonaEditForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('detalles_persona', persona_id=persona.id)
    else:
        form = PersonaEditForm(instance=persona)
    
    return render(request, 'personas/editar_persona.html', {'form': form, 'persona': persona})
