from django.urls import path
from .views import alumno_list

urlpatterns = [
    path('alumno/', alumno_list, name = 'alumno_list'),
    path('alumno/<int:matricula>', alumno_list, name = 'alumno_list'),
]