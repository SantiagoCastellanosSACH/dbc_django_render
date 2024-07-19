from django.urls import path
from .views import cargos, detalles_cargo, editar_cargo, crear_cargo

urlpatterns = [
    path('cargos/', cargos, name="cargos"),
    path('cargos/detalles/<int:cargo_id>/', detalles_cargo, name="detalles_cargo"),
    path('cargos/editar/<int:cargo_id>/', editar_cargo, name="editar_cargo"),
    path('cargos/crear/', crear_cargo, name="crear_cargo"),
]
