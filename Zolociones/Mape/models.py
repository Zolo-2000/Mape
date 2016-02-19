from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    user_name = models.CharField(max_length=13, blank=True)
    birthday = models.DateField(null=True, blank=True)
    identification = models.BigIntegerField(blank=True, null= True)
    image = models.ImageField(upload_to="media_profile", null=True, blank=True)
    def __unicode__(self):
    	return unicode(self.user)
    
class Event(models.Model):
	name = models.CharField(max_length=100)
	info = models.TextField(null=False, blank=False)
	when = models.DateField(null=False, blank=False)
	ends = models.DateField(null=True, blank=True)
	cover_image = models.ImageField(null=True, blank=True, upload_to="media_event")
	EVENT_STATE  =  ( 
        ( '10' ,  'Public' ), 
        ( '20' ,  'Private' ), 
        ( '21' ,  'Whit invitation' ),
        ( '12' ,  'Public is coming' ), 
        ( '22' ,  'Private is coming' ), 
        ( '13' ,  'Public Canceled' ), 
        ( '23' ,  'Private Canceled' ), 
        ( '14' ,  'Public Completed' ), 
        ( '24' ,  'Private Completed' ), 
    ) 
	state = models.IntegerField(choices=EVENT_STATE)
	date_joined = models.DateField(auto_now_add=True)
	guests = models.OneToOneField(Profile, null=True, blank=True)
	user = models.ForeignKey(User)
	def __unicode__(self):
		return unicode(self.name)

class Commertial(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(null=False, blank=False)
	date_joined = models.DateField(null=False, blank=False, auto_now_add=True)
	commertial_image = models.ImageField(upload_to="media_commertial")
	latitude = models.DecimalField(null=True, decimal_places=15, max_digits=19)
	longitude = models.DecimalField(null=True, decimal_places=15, max_digits=19)
	price_initial = models.DecimalField(decimal_places=2, max_digits=9)
	price_final = models.DecimalField(decimal_places=2, max_digits=9)
	user = models.ForeignKey(User)
	def __unicode__(self):
		return unicode(self.name)

class Sponsor(models.Model):
	event = models.ForeignKey('Event')
	commertial = models.ForeignKey('Commertial') 

class Offer(models.Model):
	name = models.CharField(max_length=25)
	def __unicode__(self):
		return unicode(self.name)

class Commertial_offer(models.Model):
	commertial = models.ForeignKey(Commertial)
	offer = models.ForeignKey(Offer)

class Categorie(models.Model):
	name = models.CharField(max_length=100)
	def __unicode__(self):
		return unicode(self.name)

class Commertial_categorie(models.Model):
	categorie = models.ForeignKey(Categorie)
	commertial = models.ForeignKey(Commertial)

class Hashtag(models.Model):
	name = models.CharField(max_length=100)
	event = models.ForeignKey('Event')
	def __unicode__(self):
		return unicode(self.name)
