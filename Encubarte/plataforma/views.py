# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict
from django.contrib.auth import login, authenticate, logout
from Encubarte.plataforma.models import Registro, DatosFamiliaMayor, DatosFamiliaMenor, Profesor, Horario, Curso, Grupo
from Encubarte.plataforma.parametros import parametros
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,InvalidPage
import re, math, os, ast
from datetime import datetime

def inicioControl(request, registerSuccess=False):
	conectado=False
	nombre=""
	misionInicio= "blabla"
	visionInicio= "blublu"
	quienesSomosInicio= "bleble"
	if request.user.is_authenticated():
		conectado=True
		nombre=request.user.username
	return render_to_response ('inicio.html',locals(), context_instance = RequestContext(request))

def registroControl(request):
	if not request.user.is_authenticated():
		generos = parametros["generos"]
		tiposDocumento = parametros["tiposDocumento"]
		if request.method == 'POST':
			#Toma de datos
			numeroDocumento = request.POST["numeroDocumento"]
			tipoDocumento = request.POST["tipoDocumento"]
			contrasena = request.POST["contrasena"]
			contrasena2 = request.POST["contrasena2"]
			correoElectronico = request.POST["correoElectronico"]
			nombres = request.POST["nombres"]
			apellidos = request.POST["apellidos"]
			fechaNacimiento = request.POST['fechaNacimiento']
			genero = request.POST['genero']
			direccion = request.POST['direccion']
			barrio = request.POST['barrio']
			zona = request.POST['zona']
			comuna = request.POST['comuna']
			telefonos = request.POST['telefonos']
			grupoEtnico = request.POST['grupoEtnico']
			condicion = request.POST['condicion']
			seguridadSocial = request.POST['seguridadSocial']

			#Validaciones
			errorContrasena= (request.POST["contrasena"]!=request.POST["contrasena2"])

			if (errorContrasena):
				return render_to_response('registro.html', locals(), context_instance = RequestContext(request))

			#Guardar usuario
			usuario = User.objects.create_user(username=numeroDocumento, email=correoElectronico, password=request.POST["contrasena"])
			usuario.first_name = nombres
			usuario.last_name = apellidos
			usuario.save()

			#Guardo registro
			registro = Registro(user = usuario, nombres = nombres, apellidos = apellidos, tipo = tipo, 
								fecha = fecha, edad = edad, genero = genero, direccion = direccion, barrio = barrio, 
								zona = zona, comuna = comuna, telefonos = telefonos, correo = correo, 
								grupo = grupo, condicion = condicion, seguridad = seguridad)
			registro.save()

			return inicioControl(request,registerSuccess=True)
		else:
			return render_to_response('registro.html', locals(), context_instance = RequestContext(request))
	else:
		conectado = True
		nombreUsuario = request.user.username
		return render_to_response('registro.html', locals(), context_instance = RequestContext(request))

def loginControl(request):
	try:
		username = request.POST['username']
		password = request.POST['password']
		if '@' in username:
			correo = username
			username = User.objects.get(email=correo).username

		usuario = authenticate(username=username, password=password)
		if usuario is not None and usuario.is_active:
			login(request, usuario)
			usuario = request.user
			conectado= True
			if request.user.is_superuser:
				return HttpResponseRedirect('/admin')
			return HttpResponseRedirect('/')
	except:
		return HttpResponseRedirect('/')
	loginFailed = True
	misionInicio= "blue"
	visionInicio= "red"
	quienesSomosInicio= "yellow"
	return render_to_response('inicio.html', locals(), context_instance = RequestContext(request))