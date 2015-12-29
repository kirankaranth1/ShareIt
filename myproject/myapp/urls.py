# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('myproject.myapp.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^email_url/$', 'email_url', name='email_url'),
    url(r'^thank_you/$', 'thank_you', name='thank_you'),
)
