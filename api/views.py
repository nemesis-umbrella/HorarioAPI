from django.shortcuts import render
from rest_framework import generics
from api.models import DtAlumno, CtEstado, CtCarrera
from .serializers import DtAlumnoSerializerDisplay, DtAlumnoSerializerCreateOrUpdate, CtEstadoSerializer, CtCarreraSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, authentication_classes, permission_classes

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