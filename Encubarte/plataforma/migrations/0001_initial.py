# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-23 15:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DatosFamiliaMayor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombrePadre', models.CharField(max_length=50)),
                ('nombreMadre', models.CharField(max_length=50)),
                ('telefonoPadre', models.IntegerField(max_length=20)),
                ('telefonoMadre', models.IntegerField(max_length=20)),
                ('desempeño', models.CharField(max_length=50)),
                ('lugar', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DatosFamiliaMenor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombrePadre', models.CharField(max_length=50)),
                ('nombreMadre', models.CharField(max_length=50)),
                ('telefonoPadre', models.IntegerField(max_length=20)),
                ('telefonoMadre', models.IntegerField(max_length=20)),
                ('institucionEducativa', models.CharField(max_length=50)),
                ('grupo', models.CharField(max_length=50)),
                ('jornada', models.CharField(max_length=50)),
                ('nombreAcudiente', models.CharField(max_length=50)),
                ('cedulaAcudiente', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idCurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.Curso', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dia', models.CharField(max_length=20)),
                ('horarioIni', models.CharField(max_length=20)),
                ('horarioFin', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField(max_length=11)),
                ('genero', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('tipoDocumento', models.CharField(max_length=10)),
                ('fechaNacimiento', models.DateField()),
                ('edad', models.IntegerField(max_length=4)),
                ('genero', models.CharField(max_length=1)),
                ('direccion', models.CharField(max_length=50)),
                ('barrio', models.CharField(max_length=50)),
                ('zona', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('telefonos', models.CharField(max_length=50)),
                ('telefonoFijo', models.IntegerField(max_length=20)),
                ('telefonoCelular', models.IntegerField(max_length=20)),
                ('correoElectronico', models.CharField(max_length=50)),
                ('grupoEtnico', models.CharField(max_length=50)),
                ('condicion', models.CharField(max_length=50)),
                ('seguridadSocial', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='grupo',
            name='idHorario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.Horario', unique=True),
        ),
        migrations.AddField(
            model_name='grupo',
            name='idProfesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.Profesor', unique=True),
        ),
        migrations.AddField(
            model_name='grupo',
            name='idRegistro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.Registro', unique=True),
        ),
        migrations.AddField(
            model_name='datosfamiliamenor',
            name='idRegistro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.Registro', unique=True),
        ),
        migrations.AddField(
            model_name='datosfamiliamayor',
            name='idRegistro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.Registro', unique=True),
        ),
    ]
