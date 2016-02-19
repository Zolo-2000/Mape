from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /mape/
    url(r'^$', views.index, name='index'),
    url(r'^$mape/', views.mape_view, name='mape'),
]