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
from django.urls import reverse
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
        alumno_horario = AlumnoHorario.objects.filter(alumno=alumno,activo=True)
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
                'sabado' : horario.clase_horario.sabado
            }
            clases.append(dict_horario)
            contador += 1
        return render(request,'asistencia/alumno/horario.html', {'clases' : clases})
    else:
        raise Http404("No existe la consulta")
    
@login_required
def listar_asistencia(request, id_clase = None, id_alum_horario = None):
    if request.method == 'GET':
        user_id = request.user.id
        user = get_object_or_404(User, pk=user_id)
        datos_dict = {}
        es_alumno = False
        if user.has_perm('api.es_alumno') or user.has_perm('api.es_profesor'):
            if user.has_perm('api.es_alumno'):
                es_alumno = True
                if request.GET.get('id_horario'):
                    id_horario = int(request.GET['id_horario'])
                else:
                    id_horario = None
                # Esta sección es para llenar los datos del combo de selección
                alumno = get_object_or_404(Alumno,matricula=user.get_username())
                alumno_horario = AlumnoHorario.objects.filter(alumno=alumno,activo=True)
                datos_dict['alumno_materias'] = alumno_horario
                # Datos que corresponden a la tabla
                if id_horario != None:
                    asistencia = Asistencia.objects.filter(alumno_horario=id_horario)
                else:
                    asistencia = Asistencia.objects.filter(alumno_horario__in=alumno_horario)
                datos_dict['alumno_asistencias'] = asistencia
                datos_dict['id_horario'] = id_horario
            elif user.has_perm('api.es_profesor'):
                profesor = get_object_or_404(Profesor,clave_empleado=user.get_username())
                clase_horario = get_object_or_404(ClaseHorario,profesor=profesor,id_clase_horario=id_clase)
                alumno_horario = AlumnoHorario.objects.filter(id_alum_horario=id_alum_horario,clase_horario=clase_horario)
                asistencia = Asistencia.objects.filter(alumno_horario__in=alumno_horario)
                if alumno_horario:
                    nombre_alumno = alumno_horario[0].alumno
                else:
                    nombre_alumno = None
                datos_dict['nombre_alumno'] = nombre_alumno
                datos_dict['alumno_asistencias'] = asistencia
            datos_dict['es_alumno'] = es_alumno
            return render(request,'asistencia/alumno/asistencia.html', datos_dict)
        else:
            raise Http404("No existe la consulta")
    else:
        raise Http404("No existe la operación")

@login_required
def listar_clases_profesor(request):
    if request.method == 'GET':
        user_id = request.user.id
        user = get_object_or_404(User, pk=user_id)
        if user.has_perm('api.es_profesor'):
            profesor = get_object_or_404(Profesor,clave_empleado=user.get_username())
            clase_horarios = ClaseHorario.objects.filter(profesor=profesor,activo=True)
            contador = 1
            clases = []
            for clase_horario in clase_horarios:
                asistencias = Asistencia.objects.values('fecha').filter(clase_horario=clase_horario).exclude(fecha__isnull=True).order_by('fecha').distinct('fecha')
                dict_clase = {
                    'no' : contador,
                    'url_clase' : reverse('asistencia:clase_alumnos', kwargs={'id_clase': clase_horario.id_clase_horario}), 
                    'materia' : clase_horario.materia,
                    'lunes' : clase_horario.lunes,
                    'martes' : clase_horario.martes,
                    'miercoles' : clase_horario.miercoles,
                    'jueves' : clase_horario.jueves,
                    'viernes' : clase_horario.viernes,
                    'sabado' : clase_horario.sabado,
                    'total_asist': len(asistencias),
                }
                clases.append(dict_clase)
                contador += 1
            return render(request,'asistencia/profesor/clases.html', {'clases' : clases})
        else:
            raise Http404("No existe la consulta")
    else:
        raise Http404("No existe la operación")

@login_required
def listar_clase_alumnos(request, id_clase=None):
    if request.method == 'GET':
        user_id = request.user.id
        user = get_object_or_404(User, pk=user_id)
        if user.has_perm('api.es_profesor'):
            profesor = get_object_or_404(Profesor,clave_empleado=user.get_username())
            clase_horario = get_object_or_404(ClaseHorario,profesor=profesor,id_clase_horario=id_clase)
            alumnos = AlumnoHorario.objects.filter(clase_horario=clase_horario)
            contador = 1
            list_alumno = []
            for alumno_horario in alumnos:
                asistencias = Asistencia.objects.filter(alumno_horario=alumno_horario).exclude(puntualidad=0).count()
                dict_alumno = {
                    'no' : contador,
                    'nombre' : alumno_horario.alumno.apellidos + ' ' + alumno_horario.alumno.nombre,
                    'matricula' : alumno_horario.alumno.matricula,
                    'asistencias' : asistencias,
                    'alumno_url' : reverse('asistencia:asistencia_list_clase', kwargs={'id_clase': id_clase, 'id_alum_horario' : alumno_horario.id_alum_horario}), 
                }
                print(dict_alumno['alumno_url'])
                list_alumno.append(dict_alumno)
                contador += 1
            return render(request,'asistencia/profesor/clase_alumnos.html', {'lista' : list_alumno})
        raise Http404("No existe la consulta")
    else:
        raise Http404("No existe la operación")