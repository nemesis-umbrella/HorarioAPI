from django.urls import path
from .views import perfil, listar_horario, listar_asistencia

urlpatterns = [
    path('alumno/', perfil, name = 'perfil'),
    path('alumno/horario/', listar_horario, name = 'horario_list'),
    path('alumno/asistencia/', listar_asistencia, name = 'asistencia_list'),
]