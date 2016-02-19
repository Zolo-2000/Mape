from django.shortcuts import render, redirect
from django.template.context import RequestContext
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Profile, User, Event
# Create your views here.

def mape_view(request):
	event_list = Event.objects.all()
	context = {'event_list': event_list}
	return render(request, 'mape/mape.html', context)

def index(request):
    if request.user.is_authenticated():
        return render(request, 'mape/mape.html')
    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('Mape.mape_view'))
            else:
                mensaje = 'La cuenta se encuentra desactivada.'
                return render(request, 'mape/index.html', {'mensaje': mensaje})
            pass
            mensaje = 'Nombre de usuario o contrasea no valido'
    return render(request, 'mape/index.html', {'mensaje': mensaje})
