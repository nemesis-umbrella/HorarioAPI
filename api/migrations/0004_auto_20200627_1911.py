# Generated by Django 3.0.6 on 2020-06-28 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200627_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='puntualidad',
            field=models.BooleanField(default=False, max_length=1),
        ),
    ]
