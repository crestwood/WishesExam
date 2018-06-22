from django.conf.urls import url
from . import views           # This line is new!This explicitly imports views.py in the current folder.
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^additempage$', views.additempage),
    url(r'^additem$', views.additem),
    url(r'^logout$', views.logout),
    url(r'^showitem$', views.showitem),
    url(r'^addToList', views.addToList),


    
    
]