from django.contrib import admin
from .models import User, Event, Profile, Commertial, Sponsor, Offer, Commertial_categorie, Commertial_offer, Categorie, Hashtag

class EventInLine(admin.TabularInline):
	model = Event
	extra = 3

class CategoriesStacked(admin.StackedInline):
	model = Commertial_categorie
	extra = 3

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'birthday', 'identification')
	list_filter = ('user_name',)
	search_fields = ('user',)
	inlines = [EventInLine]

class CommertialAdmin(admin.ModelAdmin):
	list_display = ('user', 'name', 'date_joined', 'price_initial', 'price_final')
	search_fields = ('name', 'price_initial')
	inlines = [CategoriesStacked]

class EventAdmin(admin.ModelAdmin):
	list_display = ('name', 'user', 'info', 'date_joined')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Commertial, CommertialAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Categorie)
admin.site.register(Sponsor)
admin.site.register(Commertial_categorie)
admin.site.register(Hashtag)
admin.site.register(Commertial_offer)