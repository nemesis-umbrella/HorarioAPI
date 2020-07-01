from django.shortcuts import render
from api.models import Alumno, AlumnoHorario, Profesor, ClaseHorario, AlumnoHorario, Asistencia
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404
from requests.models import Response
from rest_framework import status
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def index(request):
    return render(request,'asistencia/index.html')

@login_required
def perfil(request):
    user_id = request.user.id
    user = get_object_or_404(User, pk=user_id)
    if user.has_perm('api.es_alumno'):
        alumno = get_object_or_404(Alumno,matricula=user.get_username())
        total_materias = AlumnoHorario.objects.filter(alumno=alumno).count()
        return render(request,'asistencia/alumno/perfil.html', {'alumno' : alumno, 'total_materias' : total_materias})
    elif user.has_perm('api.es_profesor'):
        profesor = get_object_or_404(Profesor,clave_empleado=user.get_username())
        total_clases = ClaseHorario.objects.filter(profesor=profesor).count()
        return render(request,'asistencia/profesor/perfil.html', {'profesor' : profesor, 'total_clases' : total_clases})
    else:
        raise Http404("No existe la consulta")


@login_required
def listar_horario(request):
    user_id = request.user.id
    user = get_object_or_404(User, pk=user_id)
    if user.has_perm('api.es_alumno'):
        clases = []
        alumno = get_object_or_404(Alumno,matricula=user.get_username())
        alumno_horario = AlumnoHorario.objects.filter(alumno=alumno,estado=1)
        contador = 1
        for horario in alumno_horario:
            dict_horario = {
                'no' : contador,
                'materia' : horario.clase_horario.materia,
                'profesor' : horario.clase_horario.profesor,
                'lunes' : horario.clase_horario.lunes,
                'martes' : horario.clase_horario.martes,
                'miercoles' : horario.clase_horario.miercoles,
                'jueves' : horario.clase_horario.jueves,
                'viernes' : horario.clase_horario.viernes,
                'sabado' : horario.clase_horario.sabado,
                'estado' : horario.clase_horario.estado
            }
            clases.append(dict_horario)
            contador += 1
        return render(request,'asistencia/alumno/horario.html', {'clases' : clases})
    else:
        raise Http404("No existe la consulta")
    
@login_required
def listar_asistencia(request):
    if request.method == 'POST' or request.method == 'GET':
        user_id = request.user.id
        user = get_object_or_404(User, pk=user_id)
        if user.has_perm('api.es_alumno'):
            datos_dict = {}
            if request.method == 'POST':
                id_horario = int(request.POST['asistenciaselect']) if request.POST['asistenciaselect'] != "" else None
            else:
                id_horario = None
            # Esta sección es para llenar los datos del combo de selección
            alumno = get_object_or_404(Alumno,matricula=user.get_username())
            alumno_horario = AlumnoHorario.objects.filter(alumno=alumno,estado=1)
            datos_dict['alumno_materias'] = alumno_horario
            # Datos que corresponden a la tabla
            if id_horario != None:
                asistencia = Asistencia.objects.filter(alumno_horario=id_horario)
            else:
                asistencia = Asistencia.objects.filter(alumno_horario__in=alumno_horario)
            datos_dict['alumno_asistencias'] = asistencia
            datos_dict['id_horario'] = id_horario
            print(id_horario)
            return render(request,'asistencia/alumno/asistencia.html', datos_dict)
        else:
            raise Http404("No existe la consulta")
    else:
        raise Http404("No existe la operación")