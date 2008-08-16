# -*- coding: utf-8 -*-
import os

from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^katalog/', include('catalogue.urls')),
    
    # Panel administracyjny
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/(.*)$', admin.site.root),
    
    # Użytkownicy
    url(r'^uzytkownicy/zaloguj/$', 'django.contrib.auth.views.login', {'template_name': 'auth/login.html'}, name='login'),
    url(r'^uzytkownicy/wyloguj/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    
    # Pliki statyczne
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': os.path.join(os.path.dirname(__file__), 'media'), 'show_indexes': True}),
    url(r'^$', 'django.views.generic.simple.redirect_to', {'url': 'katalog/'}),
)
