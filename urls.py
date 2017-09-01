from django.conf.urls import *
from SystemApp import views

urlpatterns = [
     url(r'^$', views.home.as_view(), name='home'),
     url(r'^devices/$', views.devices, name='devices'),
     url(r'^index/$', views.home.as_view(), name='home'),
     url(r'^Vulnerability/$', views.Vul, name='Vulnerabilty'),
     url(r'^View Ports/$', views.ViewP, name='View Ports'),
     url(r'^search/$', views.index_search, name='search'),
     url(r'^add/$', views.add_pc, name='add'),


]