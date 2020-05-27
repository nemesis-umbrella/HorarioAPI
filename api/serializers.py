from rest_framework import serializers
from .models import DtAlumno

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