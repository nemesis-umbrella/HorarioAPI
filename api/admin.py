from django.contrib import admin
from .models import Alumno, Profesor, Materia, ClaseHorario, Carrera, AlumnoHorario, Asistencia, Grupo

# Configuración de admin para cada modelo
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nombre', 'apellidos','activo','carrera')
    list_filter = ('carrera','activo')
    search_fields = ['matricula','nombre','apellidos']

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('clave_empleado', 'nombre', 'apellidos','activo')
    list_filter = ('activo',)
    search_fields = ['clave_empleado','nombre','apellidos']

class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'creditos')
    list_filter = ('creditos',)
    search_fields = ['nombre']

class CarreraAdmin(admin.ModelAdmin):
    list_display = ('clave_carrera','carrera')
    search_fields = ['clave_carrera','descripcion']

class GrupoAdmin(admin.ModelAdmin):
    list_display = ('id_grupo', 'carrera','activo')
    list_filter = ('carrera','activo')
    search_fields = ['id_grupo','carrera']

class ClaseHorarioAdmin(admin.ModelAdmin):
    list_display = ('id_clase_horario','materia','profesor','grupo','lunes','martes','miercoles','jueves','viernes','sabado','activo')
    list_display_links = ('id_clase_horario','materia')
    list_filter = ('materia','activo')
    search_fields = ['id_clase_horario','profesor__nombre','profesor__apellidos','materia__nombre']

class AlumnoHorarioAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'clase','profesor','activo')
    list_filter = ('clase_horario__materia','activo')
    search_fields = ['alumno__matricula','alumno__nombre','alumno__apellidos','clase_horario__materia__nombre','clase_horario__profesor__nombre','clase_horario__profesor__apellidos']

class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('no_asistencia','alumno','materia','profesor','fecha','hora_entrada','hora_salida','puntualidad')
    list_filter = ('alumno_horario__clase_horario__materia','puntualidad')
    search_fields = ['alumno_horario__alumno__matricula',
                     'alumno_horario__alumno__nombre',
                     'alumno_horario__alumno__apellidos',
                     'alumno_horario__clase_horario__materia__nombre',
                     'alumno_horario__clase_horario__profesor__nombre',
                     'alumno_horario__clase_horario__profesor__apellidos']

# Register your models here.
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(ClaseHorario, ClaseHorarioAdmin)
admin.site.register(Carrera, CarreraAdmin)
admin.site.register(AlumnoHorario, AlumnoHorarioAdmin)
admin.site.register(Asistencia, AsistenciaAdmin)
admin.site.register(Grupo, GrupoAdmin)