from django.db import models

# Create your models here.

# Definición de las tablas y representación de los datos en clases
class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True, blank=False, null=False)
    nombre = models.CharField(blank=True, null=True, max_length=50)
    creditos = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']

# Modelos para la BD
class Carrera(models.Model):
    clave_carrera = models.CharField(primary_key=True, blank=False, null=False, max_length=5)
    descripcion = models.CharField(blank=True, null=True, max_length=50)
    materias = models.ManyToManyField(Materia, help_text='Seleccione las materias')

    def __str__(self):
        return self.descripcion

    @property
    def carrera(self):
        return self.descripcion

    class Meta:
        ordering = ['descripcion']


class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True, blank=False, null=False)
    descripcion = models.CharField(blank=True, null=True, max_length=50)

    def __str__(self):
        return self.descripcion

    class Meta:
        ordering = ['descripcion']


class Alumno(models.Model):
    matricula = models.CharField(primary_key=True, blank=False, null=False, max_length=11)  # This field type is a guess.
    nombre = models.CharField(max_length=50, blank=True, null=False)
    apellidos = models.CharField(max_length=100, blank=True, null=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, null=True)

    @property
    def estado_desc(self):
        return self.estado.descripcion

    @property
    def carrera_desc(self):
        return self.carrera.descripcion

    def __str__(self):
        return str(self.matricula) + ' - ' + self.nombre + ' ' + self.apellidos

    class Meta:
        ordering = ['nombre','apellidos']

class Profesor(models.Model):
    clave_empleado = models.CharField(primary_key=True, blank=False, null=False, max_length=11)
    nombre = models.CharField(blank=True, null=True, max_length=50)
    apellidos = models.CharField(blank=True, null=True, max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{0} {1}'.format(self.nombre,self.apellidos) 

    class Meta:
        verbose_name = "Maestro"
        ordering = ['nombre','apellidos']

# Tablas dependientes

class ClaseHorario(models.Model):
    id_clase_horario = models.AutoField(primary_key=True, blank=False, null=False)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=False)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=False)
    lun_ini = models.TimeField(blank=True, null=True)
    lun_fin = models.TimeField(blank=True, null=True)
    mar_ini = models.TimeField(blank=True, null=True)
    mar_fin = models.TimeField(blank=True, null=True)
    mie_ini = models.TimeField(blank=True, null=True)
    mie_fin = models.TimeField(blank=True, null=True)
    jue_ini = models.TimeField(blank=True, null=True)
    jue_fin = models.TimeField(blank=True, null=True)
    vie_ini = models.TimeField(blank=True, null=True)
    vie_fin = models.TimeField(blank=True, null=True)
    sab_ini = models.TimeField(blank=True, null=True)
    sab_fin = models.TimeField(blank=True, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)

    @property
    def lunes(self):
        if self.lun_ini != None and self.lun_fin != None:
            return ('{0} - {1}').format(self.lun_ini,self.lun_fin) 
        else:
            return '-'
    
    @property
    def martes(self):
        if self.mar_ini != None and self.mar_fin != None:
            return ('{0} - {1}').format(self.mar_ini,self.mar_fin)
        else:
            return '-'

    @property
    def miercoles(self):
        if self.mie_ini != None and self.mie_fin != None:
            return ('{0} - {1}').format(self.mie_ini,self.mie_fin)
        else:
            return '-'

    @property
    def jueves(self):
        if self.jue_ini != None and self.jue_fin != None:
            return ('{0} - {1}').format(self.jue_ini,self.jue_fin)
        else:
            return '-'

    @property
    def viernes(self):
        if self.vie_ini != None and self.vie_fin != None:
            return ('{0} - {1}').format(self.vie_ini,self.vie_fin)
        else:
            return '-'

    @property
    def sabado(self):
        if self.sab_ini != None and self.sab_fin != None:
            return ('{0} - {1}').format(self.sab_ini,self.sab_fin)
        else:
            return '-'

    def __str__(self):
        return self.profesor.clave_empleado + ' - ' + self.profesor.nombre + ' '+ self.profesor.apellidos + ' - ' + self.materia.nombre

    class Meta:
        verbose_name = "Clase horario"
        ordering = ['id_clase_horario']

class AlumnoHorario(models.Model):
    id_alum_horario = models.AutoField(primary_key=True, blank=False, null=False)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, null=False)
    clase_horario = models.ForeignKey(ClaseHorario, on_delete=models.CASCADE, null=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=False)

    @property
    def clase(self):
        return self.clase_horario.materia

    @property
    def profesor(self):
        return self.clase_horario.profesor

    def __str__(self):
        return self.alumno.matricula + ' - ' + self.alumno.nombre + ' ' + self.alumno.apellidos + ' - ' + self.clase_horario.materia.nombre

    class Meta:
        verbose_name = "Alumno Horario"
        ordering = ['id_alum_horario']

class Asistencia(models.Model):
    no_asistencia = models.AutoField(primary_key=True, blank=False, null=False)
    alumno_horario = models.ForeignKey(AlumnoHorario, on_delete=models.CASCADE, null=False)
    fecha = models.DateField(blank=True, null=False)
    hora_entrada = models.TimeField(blank=True, null=False)
    hora_salida = models.TimeField(blank=True, null=True)
    puntualidad = models.BooleanField(blank=False, null=False, max_length=1, default=False)

    @property
    def alumno(self):
        return self.alumno_horario.alumno

    @property
    def materia(self):
        return self.alumno_horario.clase_horario.materia

    def profesor(self):
        return self.alumno_horario.clase_horario.profesor

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.no_asistencia, self.alumno_horario, self.fecha)

    class Meta:
        ordering = ['-no_asistencia']
        unique_together = (('alumno_horario', 'fecha'),)


# Modelos para procesos internos (Favor de no tocar, solo en casos necesarios)

class AsistenciaAlum(object):
    def __init__(self, matricula, id_clase_horario, id_materia, clave_empleado):
        self.matricula = matricula
        self.id_clase_horario = id_clase_horario
        self.clave_empleado = clave_empleado
