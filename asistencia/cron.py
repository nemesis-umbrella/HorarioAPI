from datetime import datetime
from api.models import Asistencia, ClaseHorario, AlumnoHorario

# Pequeño ejemplo
def my_scheduled_job():
  print('La fecha y hora de ejecución:',datetime.now())


def cerrar_asistencias(fecha = None):
    """
    Este proceso se corre en segundo plano a una hora determinada. Para realizar el cierre de las asistencias.
    De esta forma se indica que alumnos faltaron a una clase. 
    """
    # Verficia si fecha se dío como parametro, sino toma la fecha del día
    if fecha == None:
        fecha = datetime.now().date()

    # Búsqueda de las clases que tuvieron asistencias
    clase_horario_ids = Asistencia.objects.filter(fecha=fecha).values('clase_horario').order_by('clase_horario_id').distinct('clase_horario_id','fecha')
    clase_horarios = ClaseHorario.objects.filter(id_clase_horario__in=clase_horario_ids)
    # Busqueda de los alumnos que no tuvieron asistencia durante el día en cada una de las clases
    for clase_horario in clase_horarios:
        alumnos_con_asistencia =  Asistencia.objects.filter(clase_horario=clase_horario,fecha=fecha).values('alumno_horario')
        alumnos_sin_asistencia = AlumnoHorario.objects.filter(clase_horario=clase_horario,activo=True).exclude(id_alum_horario__in=alumnos_con_asistencia)
        for alumno_horario in alumnos_sin_asistencia:
            alumno_reg = Asistencia(alumno_horario=alumno_horario,clase_horario=clase_horario,fecha=fecha,puntualidad=0)
            alumno_reg.save()
        
    