# Generated by Django 3.0.8 on 2020-07-25 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20200723_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='puntualidad',
            field=models.IntegerField(default=0),
        ),
    ]
