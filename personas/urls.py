from django.urls import path
from .views import personas, detalles_persona, editar_persona, crear_persona

urlpatterns = [
    path('', personas, name="personas"),
    path('personas/detalles/<int:persona_id>/', detalles_persona, name="detalles_persona"),
    path('personas/<int:id>/editar/', editar_persona, name='editar_persona'),
    path('personas/crear/', crear_persona, name="crear_persona"),
]
