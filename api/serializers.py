from rest_framework import serializers
from .models import DtAlumno, CtEstado, CtCarrera

# Configuración para alumno
class DtAlumnoSerializerDisplay(serializers.ModelSerializer):
    estado = serializers.ReadOnlyField()
    carrera = serializers.ReadOnlyField()
    class Meta:
        model = DtAlumno
        fields = [
            'matricula',
            'nombre',
            'apellidos', 
            'estado', 
            'carrera',
        ]

class DtAlumnoSerializerCreateOrUpdate(serializers.ModelSerializer):
    class Meta:
        model = DtAlumno
        fields = [
            'matricula',
            'nombre',
            'apellidos', 
            'id_estado', 
            'clave_carrera',
        ]

# Generales (Contiene datos de catálogos)
class CtEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CtEstado
        fields = [
            'id_estado',
            'descripcion',
        ]

class CtCarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = CtCarrera
        fields = [
            'clave_carrera',
            'descripcion',
        ]