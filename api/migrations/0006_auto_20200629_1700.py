# Generated by Django 3.0.6 on 2020-06-29 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200629_1056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profesor',
            options={'ordering': ['nombre', 'apellidos'], 'permissions': [('es_profesor', 'Es profesor')], 'verbose_name': 'Maestro'},
        ),
    ]
