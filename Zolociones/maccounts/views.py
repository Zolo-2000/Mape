from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
import datetime
from mapbox import Geocoder

from .forms import RegisterUserForm, ProfileRegisterForm
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
    context = None
    messages.success(request,"Su perfil a sido modificado con exito...")
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
    if request.user.is_authenticated():
        return redirect(reverse('Mape:mapa'))
    context = None
    datas = {}
    if request.POST:
        form = ProfileRegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            datas['username'] = form.cleaned_data['username']
            datas['email'] = form.cleaned_data['email']
            datas['password'] = form.cleaned_data['password']
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
            usernamesalt = datas['username']
            if isinstance(usernamesalt, unicode):
                usernamesalt = usernamesalt.encode('utf8')
            datas['activation_key']= hashlib.sha1(salt+usernamesalt).hexdigest()
            datas['email_path']="/ActivationEmail.txt"
            datas['email_subject']="Activaci&oacute;n de su cuenta"
            
            form.sendEmail(datas)
            form.save(datas) #Save the user and his profile

            request.session['registered']=True #For display purposes
            return redirect(reverse('maccounts.login', kwargs={datas['username']}))
        else:
        	form = ProfileRegisterForm()
                import pdb; pdb.set_trace()
        context = {'datas': datas, 'form': form}

    return render(request, 'maccounts/profile_register.html', context)

#View called from activation email. Activate user if link didn't expire (48h default), or offer to
#send a second link if the first expired.
def activation(request, key):
    activation_expired = False
    already_active = False
    profile = get_object_or_404(User_profile, activation_key=key)
    if profile.user.is_active == False:
        if timezone.now() > profile.key_expires:
            activation_expired = True #Display: offer the user to send a new activation link
            id_user = profile.user.id
        else: #Activation successful
            profile.user.is_active = True
            profile.user.save()

    #If user is already active, simply display error message
    else:
        already_active = True #Display : error message
    return render(request, 'maccounts/activation.html', locals())

def new_activation_link(request, user_id):
    form = RegistrationForm()
    datas={}
    user = User.objects.get(id=user_id)
    if user is not None and not user.is_active:
        datas['username']=user.username
        datas['email']=user.email
        datas['email_path']="/ResendEmail.txt"
        datas['email_subject']="Nueva clave de activaci&oacute;n de su cuenta"

        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        usernamesalt = datas['username']
        if isinstance(usernamesalt, unicode):
            usernamesalt = usernamesalt.encode('utf8')
        datas['activation_key']= hashlib.sha1(salt+usernamesalt).hexdigest()

        profile = Profile.objects.get(user=user)
        profile.activation_key = datas['activation_key']
        profile.key_expires = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=2), "%Y-%m-%d %H:%M:%S")
        profile.save()

        form.sendEmail(datas)
        request.session['new_link']=True #Display: new link sent

    return redirect(home)

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