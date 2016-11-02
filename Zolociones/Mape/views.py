from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template.context import RequestContext
from django.template import Context
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q 
from mapbox import Datasets

import datetime
from maccounts.models import User_profile
from maccounts.forms import EventRegisterForm, CommertialRegisterForm, LocationRegisterForm  
from .models import * #POST, Offer, Commertial_offer, Categorie, Commertial_categorie, Event, Sponsor, Hashtag
# Esta vista requiere que haya un usuario logeado
@login_required
def mape_view(request):
    #Descrip: Vista para la pantalla principal de la aplicacion Mape
    event_list = Event.objects.all()
    location_list = Location.objects.all()
    user_events = Event.objects.filter(user=request.user)
    zero_time = datetime.datetime.now()
    user_profile = User_profile.objects.filter(user=request.user)
    if user_profile:
        user_commertial = Commertial.objects.filter(user_profile=user_profile)
    else:
        user_commertial = None
    commertial_list = Commertial.objects.all()
    #dataset_id = 'citbo4r7007bl2slqj6cha0mq'
    #dataset = Datasets.read_dataset(dataset_id).json()
    context = ({"events": event_list, 
        "zero_time": zero_time,
        "base": 'base-mape.html',
        "user_events": user_events,
        "username": request.user.username,
        "commertials": commertial_list,
        "user_commertial": user_commertial,
        "MAPBOX_ACCESS_TOKEN": 'pk.eyJ1Ijoiem9sbyIsImEiOiJ0VlphRlZFIn0.gLAS81dTkxi1W5FqVMKwXg',
        })
    
    return render_to_response("mape/mape.html", context)

def search_view(request):
    query = request.GET.get('q','')
    zero_time = datetime.datetime.now()
    context = {"query": query}
    if query:
        qset_profiles = (
            Q(event_name__icontains=query) |
            Q(hashtag__icontains=query)
            )
        qset_events = (
            Q(user_name__icontains=query) 
            )
        qset_offers = (
            Q(offer__icontains=query) 
            )
        profiles = User_profile.objects.filter(qset_profiles).distinct()
        events = Event.objects.filter(qset_events).distinct()
        offers = Offer.objects.filter(qset_offers).distinct()
        context = { 
        "profiles": profiles, 
        "events": events, 
        "offers": offers,
        "query": query
        }
    return render_to_response("mape/search.html", context)

def shower_view(request):
    zero_time = datetime.datetime.now()
    """ se necesita mostrar los eventos: con prioridad 1.- Con incitacion publicos 2.- privados, con invitacion 3.- publicos para la semana 
    4.- Localidades comerciales con mas seguidores 5.- Localidades privadas """
    user_profile = User_profile.objects.get(user=request.user)
    events = Event.objects.all()
    invitation_events = Event.objects.filter(guests = user_profile).exclude(state=13)
    invitation_events_priv = invitation_events.filter(state=20)
    invitation_events_pub = invitation_events.exclude(state=20)
    """ la variable q contiene el texto de busqueda """
    query = request.GET.get(
        'q','')
    context = {
    "base": 'base-mape.html',
    "query": query,
    "invitation_events_priv": invitation_events_priv, 
    "events": events
    }
    if query:
        """ Uso de querysets para almacenar la consulta  Base de datos """ 
        qset_profiles = (
            Q(event_name__icontains=query) |
            Q(hashtag__icontains=query)
            )
        qset_events = (
            Q(user_name__icontains=query) 
            )
        qset_offers = (
            Q(offer__icontains=query) 
            )
        profiles = User_profile.objects.filter(qset_profiles).distinct()
        events = Event.objects.filter(qset_events).distinct()
        offers = Offer.objects.filter(qset_offers).distinct()
        context = { 
        "profiles": profiles, 
        "events": events, 
        "offers": offers,
        "query": query
        }
    return render_to_response("mape/shower_event.html", context)

def event_register_view(request):
    form = EventRegisterForm()
    if request.method == 'POST':
        """ request.FILES lo usamos para traer archivos como imagenes, video, sonido, etc"""
        form = EventRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            event_name = cleaned_data.get('event_name')
            info = cleaned_data.get('info')
            when = cleaned_data.get('when')
            ends = cleaned_data.get('ends')
            cover_price = cleaned_data.get('cover_price')
            cover_image = cleaned_data.get('cover_image')
            hashtags = cleaned_data.get('hashtags')
            location = cleaned_data.get('location')
            user = request.user
            profile_model = Profile.objects.get(user.id)
            new_event = Event()
            new_event.event_name = event_name
            new_event.info = info
            new_event.when = when
            new_event.ends = ends
            new_event.cover_price = cover_price
            new_event.cover_image = cover_image
            new_event.hashtags = hashtags
            new_event.location = location
            new_event.user = user
            """ new_event.guests = profile_model """
            new_event.save()
        else:
            form = EventRegisterForm()
    context = {'form': form}
    return render(request, 'mape/event_register.html', context)

def commertial_register_view(request):
    if request.method == 'POST':
        form = RegisterCommertialForm(request.POST, request.FILES)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        commertial_name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        commertial_image = cleaned_data.get('commertial_image')
        price_initial = cleaned_data.get('price_initial')
        price_final = cleaned_data.get('price_final')
        username = cleaned_data.get('username')

def location_register_view(request):
    if request.GET:
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        print latitude
    if request.method == 'POST':
        form = LocationRegisterForm(request.POST, request.FILES)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        location_name = cleaned_data.get('name')
        offers = cleaned_data.get('description')
        categories = cleaned_data.get('commertial_image')
        date_joined = cleaned_data.get('price_initial')
        image = cleaned_data.get('price_final')
        latitude = cleaned_data.get('username')
        longitude
        user_profile
        subscribers

def accounts_view(request):
    # Descrip: Vista para mostrar la configuracion de las cuentas del usuario
    user_profile = User_profile.objects.get(user=request.user)
    user_commertial = Commertial.objects.filter(user_profile=user_profile)
    full_name = request.user.get_full_name()
    context = ({
        "base": 'base.html',
        "user_commertial": user_commertial,
        "user_profile": user_profile,
        "full_name": full_name,
    })
    return render_to_response("mape/accounts.html", context)

