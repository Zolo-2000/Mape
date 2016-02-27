from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterUserForm
from .models import User_profile


def logout_view(request):
	logout(request)
	messages.success(request, 'Te has desconectado de Mape')
	return redirect(reverse('Maccounts:maccounts.login'))

def login_view(request):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    if request.user.is_authenticated():
        return redirect(reverse('Mape:mape'))
    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('Mape:mape'))
                mensaje= 'usuario correcto'
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
                mensaje = 'Nombre de usuario o contrase&ntilde;a no valido'
    return render(request, 'maccounts/login.html', {'mensaje': mensaje})

def user_register_view(request):
	if request.method == 'POST':
		""" request.FILES lo usamos para traer archivos como imagenes, video, sonido, etc"""
		form = RegisterUserForm(request.POST, request.FILES)
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
        	form = RegisterUserForm()
	context = {'form': form}
	return render(request, 'maccounts/user_register.html', context)

def confirmation_view(request, username):
	return HttpResponseRedirect('<h2>{{ username }} gracias por registrarte! /n Revisa tu correo electronico para confirmar </h2>')