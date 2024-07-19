from django.urls import path
from .views import personasSST, detalles_personaSST, editar_personaSST, adjuntar_personaSST

urlpatterns = [
    path('personasSST/', personasSST, name="personasSST"),
    path('personasSST/detalles/<int:personaSST_id>/', detalles_personaSST, name="detalles_personaSST"),
    path('personasSST/editar/<int:personaSST_id>/', editar_personaSST, name="editar_personaSST"),
    path('personasSST/crear/', adjuntar_personaSST, name="adjuntar_documentoSST"),
]
