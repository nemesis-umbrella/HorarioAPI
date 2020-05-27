# Generated by Django 3.0.2 on 2020-05-26 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CtCarrera',
            fields=[
                ('clave_carrera', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'ct_carrera',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CtEstado',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'ct_estado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CtMateria',
            fields=[
                ('id_materia', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('creditos', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ct_materia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DtAlumClaseHorario',
            fields=[
                ('id_alum_clas_hor', models.AutoField(primary_key=True, serialize=False)),
                ('matricula', models.TextField(blank=True, max_length=11, null=True)),
                ('id_clase_horario', models.IntegerField(blank=True, null=True)),
                ('id_estado', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dt_alum_clase_horario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DtAlumno',
            fields=[
                ('matricula', models.TextField(max_length=11, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'dt_alumno',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DtAsistencia',
            fields=[
                ('no_asistencia', models.AutoField(primary_key=True, serialize=False)),
                ('id_alum_clas_hor', models.IntegerField(blank=True, null=True)),
                ('matricula', models.TextField(blank=True, max_length=11, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('hora_entrada', models.TimeField(blank=True, null=True)),
                ('hora_salida', models.TimeField(blank=True, null=True)),
                ('puntualidad', models.TextField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'dt_asistencia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DtCarreraMateria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave_carrera', models.CharField(max_length=5)),
                ('id_materia', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dt_carrera_materia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DtClaseHorario',
            fields=[
                ('id_clase_horario', models.AutoField(primary_key=True, serialize=False)),
                ('id_mat_prof', models.IntegerField(blank=True, null=True)),
                ('lun_ini', models.TimeField(blank=True, null=True)),
                ('lun_fin', models.TimeField(blank=True, null=True)),
                ('mar_ini', models.TimeField(blank=True, null=True)),
                ('mar_fin', models.TimeField(blank=True, null=True)),
                ('mie_ini', models.TimeField(blank=True, null=True)),
                ('mie_fin', models.TimeField(blank=True, null=True)),
                ('jue_ini', models.TimeField(blank=True, null=True)),
                ('jue_fin', models.TimeField(blank=True, null=True)),
                ('vie_ini', models.TimeField(blank=True, null=True)),
                ('vie_fin', models.TimeField(blank=True, null=True)),
                ('sab_ini', models.TimeField(blank=True, null=True)),
                ('sab_fin', models.TimeField(blank=True, null=True)),
                ('id_estado', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dt_clase_horario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DtMateriaProfesor',
            fields=[
                ('id_mat_prof', models.AutoField(primary_key=True, serialize=False)),
                ('id_materia', models.IntegerField(blank=True, null=True)),
                ('clave_empleado', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dt_materia_profesor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DtProfesor',
            fields=[
                ('clave_empleado', models.TextField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=100, null=True)),
                ('id_estado', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dt_profesor',
                'managed': False,
            },
        ),
    ]
