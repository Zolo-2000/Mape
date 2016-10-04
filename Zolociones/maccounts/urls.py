from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.login_view, name='maccounts.login'),
    url(r'^register/$', views.profile_register_view, name='maccounts.register'),
    url(r'^user_register/$', views.user_register_view, name='maccounts.user_register'),
    url(r'gracias/(?P<username>[\w]+)/$', views.confirmation_view, name='maccounts.confirmation'),
    url(r'^logout/$', views.logout_view, name='maccounts.logout'),
]