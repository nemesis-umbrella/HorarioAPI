from django.urls import path
from .views import perfil, listar_horario, listar_asistencia, listar_clases_profesor

urlpatterns = [
    path('alumno/', perfil, name = 'perfil_alumno'),
    path('alumno/horario/', listar_horario, name = 'horario_list'),
    path('alumno/asistencia/', listar_asistencia, name = 'asistencia_list'),
    path('profesor/', perfil, name = 'perfil_profesor'),
    path('profesor/clases', listar_clases_profesor, name = 'clases_profesor'),
]