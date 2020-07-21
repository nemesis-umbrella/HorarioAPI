from django.urls import path
from .views import perfil, listar_horario, listar_asistencia, listar_clases_profesor, listar_clase_alumnos

urlpatterns = [
    path('alumno/', perfil, name = 'perfil_alumno'),
    path('alumno/horario/', listar_horario, name = 'horario_list'),
    path('alumno/asistencia/', listar_asistencia, name = 'asistencia_list'),
    path('profesor/', perfil, name = 'perfil_profesor'),
    path('profesor/clases/', listar_clases_profesor, name = 'clases_profesor'),
    path('profesor/clases/<int:id_clase>/', listar_clase_alumnos, name = 'clase_alumnos'),
    path('profesor/clases/<int:id_clase>/<int:id_alum_horario>/', listar_asistencia, name = 'asistencia_list_clase'),
]