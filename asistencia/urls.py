from django.urls import path
from .views import perfil, listar_horario

urlpatterns = [
    path('alumno/', perfil, name = 'perfil'),
    path('alumno/horario', listar_horario, name = 'horario_list')
]