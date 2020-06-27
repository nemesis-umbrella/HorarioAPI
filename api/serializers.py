from rest_framework import serializers
from .models import Alumno, Estado, Carrera

# Configuración para alumno
class AlumnoSerializerDisplay(serializers.ModelSerializer):
    estado = serializers.ReadOnlyField()
    carrera = serializers.ReadOnlyField()
    class Meta:
        model = Alumno
        fields = [
            'matricula',
            'nombre',
            'apellidos', 
            'estado', 
            'carrera',
        ]

class AlumnoSerializerCreateOrUpdate(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = [
            'matricula',
            'nombre',
            'apellidos', 
            'id_estado', 
            'clave_carrera',
        ]

# Generales (Contiene datos de catálogos)
class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = [
            'id_estado',
            'descripcion',
        ]

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = [
            'clave_carrera',
            'descripcion',
        ]