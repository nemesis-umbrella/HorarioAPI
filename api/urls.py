from django.urls import path
from .views import alumno_list, estado_list, carrera_list, alumno_asistencia

urlpatterns = [
    path('alumno/', alumno_list, name = 'alumno_list'),
    path('alumno/<int:matricula>', alumno_list, name = 'alumno_list'),
    path('alumno/estados', estado_list, name = 'estado_list'),
    path('alumno/carreras', carrera_list, name = 'carrera_list'),
    path('alumno/asistencia', alumno_asistencia, name = 'alumno_asistencia'),
]