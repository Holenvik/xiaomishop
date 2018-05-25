from . import views
from django.conf.urls import url



urlpatterns = [
            url(r'^news/(?P<slug>[-\w]+)/$',
                views.article,
                name='article'),
]
