from django.db import models
from django.contrib.auth.models import User, Group
import datetime
from django.utils import timezone
from maccounts.models import User_profile

class Hashtag(models.Model):
	hashtag_name = models.CharField(max_length=45)
	def __unicode__(self):
		return unicode(self.hashtag_name)

class Categorie(models.Model):
	categorie_name = models.CharField(max_length=45, unique=True)
	def __unicode__(self):
		return unicode(self.categorie_name)

class Offer(models.Model):
	offer_name = models.CharField(max_length=45, unique=True)
	price = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True )
	product = models.BooleanField(default=True, blank=True)
	image = models.ImageField(upload_to="media", null=True, blank=True)
	def __unicode__(self):
		return unicode(self.offer_name)

class Location(models.Model):
	location_name = models.CharField(max_length=45)
	offers = models.ManyToManyField(Offer, blank=True)
	categories = models.ManyToManyField(Categorie)
	date_joined = models.DateField(null=False, blank=False, auto_now_add=True)
	image = models.ImageField(upload_to="media", null=True, blank=True)
	latitude = models.DecimalField(null=True, decimal_places=15, max_digits=19)
	longitude = models.DecimalField(null=True, decimal_places=15, max_digits=19)
	user_profile = models.ForeignKey(User)
	subscribers = models.ManyToManyField(User_profile, null=False, blank=True)
	def __unicode__(self):
		return unicode(self.location_name)

class Commertial(models.Model):
	commertial_name = models.CharField(max_length=45, unique=True)
	location = models.OneToOneField(Location, on_delete=models.CASCADE)
	ruc = models.BigIntegerField(blank=True, null= True)
	description = models.TextField(null=False, blank=False)
	date_joined = models.DateField(null=False, blank=False, auto_now_add=True)
	commertial_image = models.ImageField(upload_to="accounts", null=True, blank=True)
	user_profile = models.OneToOneField(User_profile)
	def __unicode__(self):
		return unicode(self.commertial_name)

class Event(models.Model):
	event_name = models.CharField(max_length=75)
	info = models.TextField(null=False, blank=False)
	when = models.DateTimeField(null=False, blank=False, auto_now_add=False)
	ends = models.DateTimeField(null=True, blank=True, auto_now_add=False)
	cover_price = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True )
	cover_image = models.ImageField(null=True, blank=True, upload_to="media_event")
	EVENT_STATE = ( 
        ( 10 , 'Public' ), 
        ( 20 , 'Private' ), 
        ( 21 , 'Whit invitation' ),
        ( 12 , 'Public is coming' ), 
        ( 22 , 'Private is coming' ),
        ( 221, 'Private with invitation is coming'),
        ( 13 , 'Public Completed' ), 
        ( 23 , 'Private Completed' ),
        ( 14 , 'Public Canceled' ), 
        ( 24 , 'Private Canceled' ), 
        ( 244, 'Private with invitation is canceled' ),
    ) 
	state = models.IntegerField(
		choices=EVENT_STATE, 
		default=20)
	date_joined = models.DateField(auto_now_add=True)
	hashtags = models.ManyToManyField(Hashtag, blank=True)
	location = models.ForeignKey(Location, null=True, blank=False)
	user = models.ForeignKey(User)
	guests = models.ManyToManyField(User_profile, null=False, blank=True)
	def __unicode__(self):
		return unicode(self.event_name)

class Post(models.Model):
	date_joined = models.DateField(null=False, blank=False, auto_now_add=True)
	image = models.ImageField(upload_to="media_event", null=True, blank=True)
	description = models.CharField(max_length=200, null=True, blank=True )
	POST_STATE  =  ( 
		( 10 , 'Event image' ),
		( 20 , 'Commertial image' ), 
        ( 30 , 'Hashtag image' ),
    ) 
	state = models.IntegerField(choices=POST_STATE)
	event = models.ForeignKey(Event)
	user = models.ForeignKey(User)
	def __unicode__(self):
		return unicode(self.description)
	class Admin:
		list_display = ('commertial_name', 'user','ruc', 'location', 'date_joined')
		list_filter = ('commertial_name', 'user')

class Sponsor(models.Model):
	event = models.ForeignKey(Event)
	commertial = models.ForeignKey(Commertial)
	STATE  =  ( 
		( 10 , 'approved' ),
		( 20 , 'pending' ), 
    ) 
	state = models.IntegerField(choices=STATE, default=20)


