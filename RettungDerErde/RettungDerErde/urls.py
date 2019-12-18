"""
Definition of urls for RettungDerErde.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls import include, url
admin.autodiscover()


import app.forms
import app.views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^about$', views.about, name='about'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^seed$', views.seed, name='seed'),

    

    path('login/',
         LoginView.as_view
        (
            template_name = 'app/login.html',
            authentication_form = app.forms.BootstrapAuthenticationForm,
            extra_context =
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        ),
        name='login'),
    url(r'^logout$',
        LogoutView.as_view
        (
            next_page = '/'
        ),
        name='logout'),

   url(r'^admin$', views.admin, name='admin'),
    
   
]
