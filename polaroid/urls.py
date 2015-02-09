__author__ = 'harshit'

from django.conf.urls import patterns, include, url
from polaroid import views

urlpatterns = patterns('',
    url(r'^$', views.Index, name='Index'),
)
