from django.contrib import admin
from .models import Alumno, Profesor, Materia, ClaseHorario, Carrera, AlumnoHorario

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Materia)
admin.site.register(ClaseHorario)
admin.site.register(Carrera)
admin.site.register(AlumnoHorario)