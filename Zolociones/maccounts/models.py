from django.db import models
from django.contrib.auth.models import User
from django import forms

class User_profile(models.Model):
    user = models.OneToOneField(User, null=False, blank=False)
    user_name = models.CharField(max_length=45, blank=False)
    birthday = models.DateField(null=True, blank=True)
    identification = models.BigIntegerField(blank=True, null= True)
    phone_1 = models.BigIntegerField(blank=True, null=True)
    phone_2 = models.BigIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to="accounts", null=True, blank=True)
    def __unicode__(self):
    	return unicode(self.user_name)

