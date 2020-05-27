from django.db import models

# Create your models here.

class CtCarrera(models.Model):
    clave_carrera = models.CharField(primary_key=True, blank=False, null=False, max_length=5)
    descripcion = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'ct_carrera'


class CtEstado(models.Model):
    id_estado = models.AutoField(primary_key=True, blank=False, null=False)
    descripcion = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'ct_estado'


class CtMateria(models.Model):
    id_materia = models.AutoField(primary_key=True, blank=False, null=False)
    nombre = models.CharField(blank=True, null=True, max_length=50)
    creditos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ct_materia'

class DtAlumClaseHorario(models.Model):
    id_alum_clas_hor = models.AutoField(primary_key=True, blank=False, null=False)
    matricula = models.TextField(blank=True, null=True, max_length=11)  # This field type is a guess.
    id_clase_horario = models.IntegerField(blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dt_alum_clase_horario'


class DtAlumno(models.Model):
    matricula = models.TextField(primary_key=True, blank=False, null=False, max_length=11)  # This field type is a guess.
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    id_estado = models.ForeignKey(CtEstado, related_name='estados', on_delete=models.CASCADE, db_column='id_estado')
    clave_carrera = models.ForeignKey(CtCarrera, related_name='carreras', on_delete=models.CASCADE, db_column ='clave_carrera')

    @property
    def estado(self):
        return self.id_estado.descripcion

    @property
    def carrera(self):
        return self.clave_carrera.descripcion

    class Meta:
        managed = False
        db_table = 'dt_alumno'


class DtAsistencia(models.Model):
    no_asistencia = models.AutoField(primary_key=True, blank=False, null=False)
    id_alum_clas_hor = models.IntegerField(blank=True, null=True)
    matricula = models.TextField(blank=True, null=True, max_length=11)  # This field type is a guess.
    fecha = models.DateField(blank=True, null=True)
    hora_entrada = models.TimeField(blank=True, null=True)
    hora_salida = models.TimeField(blank=True, null=True)
    puntualidad = models.TextField(blank=True, null=True, max_length=1)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'dt_asistencia'


class DtCarreraMateria(models.Model):
    clave_carrera = models.CharField(blank=False, null=False, max_length=5)
    id_materia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dt_carrera_materia'
        unique_together = (('clave_carrera', 'id_materia'),)


class DtClaseHorario(models.Model):
    id_clase_horario = models.AutoField(primary_key=True, blank=False, null=False)
    id_mat_prof = models.IntegerField(blank=True, null=True)
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
    id_estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dt_clase_horario'


class DtMateriaProfesor(models.Model):
    id_mat_prof = models.AutoField(primary_key=True, blank=False, null=False)
    id_materia = models.IntegerField(blank=True, null=True)
    clave_empleado = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'dt_materia_profesor'


class DtProfesor(models.Model):
    clave_empleado = models.TextField(primary_key=True, blank=False, null=False)  # This field type is a guess.
    nombre = models.CharField(blank=True, null=True, max_length=50)
    apellidos = models.CharField(blank=True, null=True, max_length=100)
    id_estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dt_profesor'