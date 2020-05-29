from django.shortcuts import render
from rest_framework import generics
from api.models import DtAlumno, CtEstado, CtCarrera, DtClaseHorario, DtAlumClaseHorario, DtAsistencia
from .serializers import DtAlumnoSerializerDisplay, DtAlumnoSerializerCreateOrUpdate, CtEstadoSerializer, CtCarreraSerializer, AsistenciaAlumSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from datetime import datetime, time
from dateutil.relativedelta import relativedelta

# Funciones generales para alumno
@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def alumno_list(request, matricula=None):
    # Métodos de obtención de datos
    if request.method in ('PUT','DELETE'):
        try:
            alumno = DtAlumno.objects.get(matricula=matricula)
        except DtAlumno.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'GET':
            if matricula != None:
                try:
                    alumnos = DtAlumno.objects.get(matricula=matricula)
                except DtAlumno.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                alumnos = DtAlumno.objects.all()

    # Operaciones asignadas a los alumnos
    if request.method == 'GET':
        if matricula != None:
            serializer = DtAlumnoSerializerCreateOrUpdate(alumnos)
            return Response(serializer.data)
        else:
            serializer = DtAlumnoSerializerDisplay(alumnos, many=True)
            return Response(serializer.data)
 
    elif request.method == 'POST':
        serializer = DtAlumnoSerializerCreateOrUpdate(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = DtAlumnoSerializerCreateOrUpdate(alumno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        alumno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Vista para registrar asistencia
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def alumno_asistencia(request):
    if request.method == 'POST':
        serializer = AsistenciaAlumSerializer(data=request.data)
        if serializer.is_valid():
            # Valida que exista la clase horario
            try:
                clase_horario = DtClaseHorario.objects.get(id_clase_horario=serializer.data.get("id_clase_horario"),id_mat_prof=serializer.data.get("id_mat_prof"))
            except DtClaseHorario.DoesNotExist:
                #print('No se encontró la clase horario')
                return Response(status=status.HTTP_404_NOT_FOUND)
            # Valida que exista el alumno
            try:
                alumno = DtAlumno.objects.get(matricula=serializer.data.get("matricula"))
            except DtAlumno.DoesNotExist:
                #print('No se encontro el alumno')
                return Response(status=status.HTTP_404_NOT_FOUND)
            # Valida que el alumno esté registrado en la clase
            try:
                alum_clase_horario = DtAlumClaseHorario.objects.get(matricula=serializer.data.get("matricula"),id_clase_horario=serializer.data.get("id_clase_horario"))
            except DtAlumClaseHorario.DoesNotExist:
                #print('El alumno no tiene la clase registrada.')
                return Response(status=status.HTTP_404_NOT_FOUND)
            # Valida que el alumno tenga la clase habilitada
            if alum_clase_horario.id_estado.id_estado != 1:
                #print('El alumno no tiene habilitada la clase')
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            # Valida día de la semana
            fecha_actual = datetime.now()
            dia_semana = datetime.weekday(fecha_actual)
            if dia_semana == 0:
                # Lunes
                hora_ini = clase_horario.lun_ini
                hora_fin = clase_horario.lun_fin
            elif dia_semana == 1:
                # Martes
                hora_ini = clase_horario.mar_ini
                hora_fin = clase_horario.mar_fin
            elif dia_semana == 2:
                # Miércoles
                hora_ini = clase_horario.mie_ini
                hora_fin = clase_horario.mie_fin
            elif dia_semana == 3:
                # Jueves
                hora_ini = clase_horario.jue_ini
                hora_fin = clase_horario.jue_fin
            elif dia_semana == 4:
                # Viernes
                hora_ini = clase_horario.vie_ini
                hora_fin = clase_horario.vie_fin
            elif dia_semana == 5:
                # Sábado
                hora_ini = clase_horario.sab_ini
                hora_fin = clase_horario.sab_fin
            # Proceso de registro
            if hora_ini != None and hora_fin != None:
                if  fecha_actual.time() >= hora_ini and  fecha_actual.time() < hora_fin :
                    fecha = fecha_actual.date()
                    try:
                        # Registro de salida
                        dt_asistencia = DtAsistencia.objects.get(matricula=alumno,fecha=fecha.isoformat(),id_alum_clas_hor=alum_clase_horario)
                        if dt_asistencia.hora_salida == None:
                            dt_asistencia.hora_salida = fecha_actual.time()
                            dt_asistencia.save()
                    except DtAsistencia.DoesNotExist:
                        # Verifica que haya llegado puntual
                        fecha_comb = datetime.combine(fecha,hora_ini)
                        diff = relativedelta(fecha_actual, fecha_comb)
                        if diff.hours < 1 and diff.minutes <= 15:
                            puntual = 1
                        else:
                            puntual = 0
                        # Registro de entrada
                        dt_asistencia = DtAsistencia(id_alum_clas_hor=alum_clase_horario,matricula=alumno,fecha=fecha.isoformat(),hora_entrada=fecha_actual.time(),puntualidad=puntual)
                        dt_asistencia.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vistas generales (cerrar sesión, catálogos)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def estado_list(request):
    if request.method == 'GET':
        estados = CtEstado.objects.all()        
        serializer = CtEstadoSerializer(estados, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def carrera_list(request):
    if request.method == 'GET':
        carreras = CtCarrera.objects.all()        
        serializer = CtCarreraSerializer(carreras, many=True)
        return Response(serializer.data)

class Logout(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self,request, format = None):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        return Response(status=status.HTTP_200_OK)