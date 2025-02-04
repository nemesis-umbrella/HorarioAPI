from rest_framework import serializers
from .models import Alumno, Carrera

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
            'estado', 
            'clave_carrera',
        ]

# Generales (Contiene datos de catálogos)
class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = [
            'clave_carrera',
            'descripcion',
        ]

# Contiene los campos para validar
class AsistenciaAlumSerializer(serializers.Serializer):
    matricula = serializers.CharField(max_length=11)
    id_clase_horario = serializers.IntegerField()
    clave_empleado = serializers.CharField(max_length=11)
