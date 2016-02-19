from django.shortcuts import render

from .forms import RegisterUserForm

def user_register_view(request):
	if request.method == 'POST':
		""" request.FILES lo usamos para traer archivos como imagenes, video, sonido, etc"""
		form = RegisterUserForm(request.POST, request.FILES)
	else:
		form = None

	context = { 'form': form}
	return render(request, 'maccounts/user_register.html', context)