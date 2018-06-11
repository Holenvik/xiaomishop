from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^about/$', views.about, name='about'),
    url(r'^delivery/$', views.delivery, name='delivery'),
    url(r'^guide/$', views.guide, name='guide'),
]
