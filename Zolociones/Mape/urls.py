from django.conf.urls import url

from . import views
from maccounts.views import logout_view

urlpatterns = [
    # ex: /mape/
    url(r'^$logout/', logout_view, name='logout'),
    url(r'^$', views.mape_view, name='mape'),
    url(r'^accounts/', views.accounts_view, name='accounts')
]