from django.urls import path
from .views import empresaSST, detalles_empresaSST, editar_empresaSST, crear_empresaSST

urlpatterns = [
    path('empresaSST/', empresaSST, name="empresaSST"),
    path('empresaSST/detalles/<int:empresaSST_id>/', detalles_empresaSST, name="detalles_empresaSST"),
    path('empresaSST/editar/<int:empresaSST_id>/', editar_empresaSST, name="editar_empresaSST"),
    path('empresaSST/crear/', crear_empresaSST, name="crear_empresaSST"),
]

