from django.contrib import admin
from .models import *
from maccounts.models import *


class PostInLine(admin.TabularInline):
	model = Post
	extra = 3

class EventAdmin(admin.ModelAdmin):
	list_display = ('event_name', 'when', 'state', 'location', 'date_joined')
	list_filter = ('event_name', 'user')
	ordering = ['-date_joined']
	search_fields = ('when', 'state', 'location', 'hashtags')

class CommertialAdmin(admin.ModelAdmin):
	list_display = ('commertial_name', 'location', 'user_profile','ruc', 'date_joined')
	list_filter = ['date_joined']
	ordering = ['commertial_name']
	search_fields = ['commertial_name', 'user_profile', 'location']

class LocationAdmin(admin.ModelAdmin):
	list_display = ('location_name', 'user_profile', 'date_joined')
	list_filter = ('user_profile', 'date_joined')

admin.site.register(Event, EventAdmin)
admin.site.register(Sponsor)
admin.site.register(Hashtag)
admin.site.register(Categorie)
admin.site.register(Commertial, CommertialAdmin)
admin.site.register(Post)
admin.site.register(Location, LocationAdmin)
admin.site.register(Offer)