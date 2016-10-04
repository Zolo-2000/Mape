from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from mapbox import Geocoder

from .forms import RegisterUserForm
from .forms import RegisterProfileForm
from Mape.models import User_profile


def email_check(user):
    return user.email.endswith('@example.com')

"""@user_passes_test(email_check)
def my_view(request):
    
"""
def logout_view(request):
	logout(request)
	messages.success(request, 'Te has desconectado de Mape')
	return redirect(reverse('Maccounts:maccounts.login'))

def login_view(request):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    mensaje = ''
    if request.user.is_authenticated():
        return redirect(reverse('Mape:mapa'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('Mape:mapa'))
            else:
                mensaje = 'La cuenta esta inactiva'
            mensaje = 'Nombre de usuario o contrase&ntilde;a no v&aacute;lido'
            context = {'mensaje': mensaje}
    return render(request, 'maccounts/login.html', context)


def profile_register_view(request):
	if request.method == 'POST':
		""" request.FILES lo usamos para traer archivos como imagenes, video, sonido, etc"""
		form = RegisterProfileForm(request.POST, request.FILES)
		if form.is_valid():
			cleaned_data = form.cleaned_data
			username = cleaned_data.get('username')
			password = cleaned_data.get('password')
			email = cleaned_data.get('email')
			image = cleaned_data.get('image')
			user_model = User.objects.create_user(username=username, password=password)
			user_model.email = email
			user_model.save()
			user_profile = User_profile()
			user_profile.user = user_model
			user_profile.user_name = username
			user_profile.image = image
			user_profile.save()
			""" Aqui: Enviar correo con codigo de activacion """
			return redirect(reverse('maccounts.confirmation', kwargs={'username': username}))
        else:
        	form = RegisterProfileForm()
	context = {'form': form}
	return render(request, 'maccounts/profile_register.html', context)

def user_register_view(request):
	if request.method == 'POST':
		""" request.FILES lo usamos para traer archivos como imagenes, video, sonido, etc"""
		form = RegisterUserForm(request.POST, request.FILES)
		if form.is_valid():
			cleaned_data = form.cleaned_data
			username = cleaned_data.get('username')
			first_name = cleaned_data.get('first_name')
			last_name = cleaned_data.get('last_name')
			identification = cleaned_data.get('identification')
			birthday = cleaned_data.get('birthday')
			phone_1 = cleaned_data.get('phone_1')
			phone_2 = cleaned_data.get('phone_2')
			photo = cleaned_data.get('photo')
			user_model = User.objects.get(id=request.user)
			profile_model = Profile.objects.get(user_model.id)
			user_model.first_name = first_name
			user_model.last_name = last_name

			user_model.save()
			user_profile = User_profile()
			user_profile.user = user_model
			user_profile.user_name = username
			user_profile.image = image
			user_profile.save()
			""" Aqui: Enviar correo con codigo de activacion """
			return redirect(reverse('maccounts.confirmation', kwargs={'username': username}))
        else:
        	form = RegisterUserForm()
	context = {'form': form}
	return render(request, 'maccounts/user_register.html', context)
def confirmation_view(request, username):
	return HttpResponseRedirect('<h2>{{ username }} gracias por registrarte! /n Revisa tu correo electronico para confirmar </h2>')