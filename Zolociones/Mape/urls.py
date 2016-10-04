from django.conf.urls import url
from maccounts.views import login_view, logout_view
from . import views

urlpatterns = [
    # ex: /mape/
    url(r'^$', views.mape_view, name='mapa'),
    url(r'^login/$', login_view, name='login'),
    url(r'^accounts/$', views.accounts_view, name='accounts'),
    url(r'^e/$', views.shower_view, name='shower'),
    url(r'^event_register/$', views.event_register_view, name='event_register'),
    url(r'^location_register/$', views.location_register_view, name='location_register'),
    url(r'^commertial_register/$', views.commertial_register_view, name='commertial_register'),
    url(r'^$search/$', views.search_view, name='search'),
    url(r'^$logout/$', logout_view, name='maccounts.logout'),
]