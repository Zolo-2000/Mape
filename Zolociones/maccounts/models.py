from django.db import models
from django.contrib.auth.models import User 
from django import forms

class User_profile(models.Model):
    user = models.OneToOneField(User)
    user_name = models.CharField(max_length=13, blank=True)
    birthday = models.DateField(null=True, blank=True)
    identification = models.BigIntegerField(blank=True, null= True)
    image = models.ImageField(upload_to="media_profile", null=True, blank=True)
    def __unicode__(self):
    	return unicode(self.user)
