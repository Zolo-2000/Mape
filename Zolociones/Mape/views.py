from django.shortcuts import render, redirect
from django.template.context import RequestContext
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Profile, User, Event
# Esta vista requiere que haya un usuario logeado
@login_required
def mape_view(request):
    # Descrip: Vista para la pantalla principal de la aplicacion Mape
	event_list = Event.objects.all()
	context = {'event_list': event_list}
	return render(request, 'mape/mape.html', context)

def accounts_view(request):
    # Descrip: Vista para mostrar la configuracion de las cuentas del usuario
    return render(request, 'mape/accounts.html')