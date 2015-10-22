from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
  url(r'^$', Home.as_view(), name='home'),
  url(r'^Message/create/$', MessageCreateView.as_view(), name='Message_create'),

)