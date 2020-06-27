from django.db import models

# Create your models here.

# Modelos para procesos internos
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
        return '{0} - {1} {2}'.format(self.clave_empleado,self.nombre,self.apellidos) 

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


    def __str__(self):
        return self.profesor.nombre + ' '+ self.profesor.apellidos + ' - ' + self.materia.nombre

    class Meta:
        verbose_name = "Clase horario"
        ordering = ['id_clase_horario']

class AlumnoHorario(models.Model):
    id_alum_horario = models.AutoField(primary_key=True, blank=False, null=False)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, null=False)
    clase_horario = models.ForeignKey(ClaseHorario, on_delete=models.CASCADE, null=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=False)

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
    puntualidad = models.TextField(blank=True, null=True, max_length=1)

    def __str__(self):
        return str(self.no_asistencia)

    class Meta:
        ordering = ['no_asistencia']