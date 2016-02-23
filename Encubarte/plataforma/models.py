from django.db import models
from django.contrib.auth.models import User

#extender de user?
#user = models.ForeignKey(User, unique=True)
class Registro(models.Model):
	user = models.ForeignKey(User, unique=True)
	#numeroDocumento = models.IntegerField(max_length=20,primary_key=True)
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	tipoDocumento = models.CharField(max_length=10)
	fechaNacimiento = models.DateField()
	edad = models.IntegerField(max_length=4)
	genero = models.CharField(max_length=1)
	direccion = models.CharField(max_length=50)
	barrio = models.CharField(max_length=50)
	zona = models.CharField(max_length=50)
	comuna = models.CharField(max_length=50)
	telefonos = models.CharField(max_length=50)
	telefonoFijo = models.IntegerField(max_length=20)
	telefonoCelular = models.IntegerField(max_length=20)
	correoElectronico = models.CharField(max_length=50)
	grupoEtnico = models.CharField(max_length=50)
	condicion = models.CharField(max_length=50)
	seguridadSocial = models.CharField(max_length=50)

	#def url(self,filename):
	#	return "fotos/carros/%s/%s/%s/%s"%(self.marca, self.referencia, self.placa , filename)
	#foto = models.FileField(upload_to=url)

	def __unicode__(self):
		return self.numeroDocumento+" "+self.nombres+" "+self.apellidos

class DatosFamiliaMayor(models.Model):
	id = models.AutoField(primary_key=True)
	idRegistro = models.ForeignKey(Registro, unique=True)
	nombrePadre = models.CharField(max_length=50)
	nombreMadre = models.CharField(max_length=50)
	telefonoPadre = models.IntegerField(max_length=20)
	telefonoMadre = models.IntegerField(max_length=20)
	desempeño = models.CharField(max_length=50)
	lugar = models.CharField(max_length=50)

class DatosFamiliaMenor(models.Model):
	id = models.AutoField(primary_key=True)
	idRegistro = models.ForeignKey(Registro, unique=True)
	nombrePadre = models.CharField(max_length=50)
	nombreMadre = models.CharField(max_length=50)
	telefonoPadre = models.IntegerField(max_length=20)
	telefonoMadre = models.IntegerField(max_length=20)
	institucionEducativa = models.CharField(max_length=50)
	grupo = models.CharField(max_length=50)
	jornada = models.CharField(max_length=50)
	nombreAcudiente = models.CharField(max_length=50)
	cedulaAcudiente = models.CharField(max_length=50)

class Profesor(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=50)
	edad = models.IntegerField(max_length=11)
	genero = models.CharField(max_length=50)

class Horario(models.Model):
	id = models.AutoField(primary_key=True)
	dia = models.CharField(max_length=20)
	horarioIni = models.CharField(max_length=20)
	horarioFin = models.CharField(max_length=20)

class Curso(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=50)

class Grupo(models.Model):
	id = models.AutoField(primary_key=True)
	idRegistro = models.ForeignKey(Registro, unique=True)
	idProfesor = models.ForeignKey(Profesor, unique=True)
	idCurso = models.ForeignKey(Curso, unique=True)
	idHorario = models.ForeignKey(Horario, unique=True)