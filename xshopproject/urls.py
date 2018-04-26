"""xshopproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from xiaomishopapp import views
from django.conf import settings
from django.contrib.auth import views as auth_views    #packeg with login and logout
from django.conf.urls.static import static


urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^$', views.home, name='home'),

    url(r'^xiaomishop/sign-in', auth_views.login,
        { 'template_name': 'xiaomishop/sign_in.html' },
        name = 'xiaomishop-sign-in'),

    url(r'^xiaomishop/account/$', views.account,
        name = 'xiaomishop-account',
    ),

    url(r'^xiaomishop/sign-out', auth_views.logout,
        {'next_page': '/'},
        name = 'xiaomishop-sign-out'),

    url(r'^xiaomishop/$', views.xiaomishop_home, name = 'xiaomishop-home'), #REDIRECT TO HOME PAGE

    url(r'^xiaomishop/sign-up/$', views.xiaomishop_sign_up, name = 'xiaomishop-sign-up'),


    url(r'^orders/', include('orders.urls', namespace='orders')),

    url(r'^', include('xiaomishopapp.urls', namespace='xiaomishop')),

    url(r'^cart/', include('cart.urls', namespace='cart')),
    #


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
