from django.urls import path
from django.conf.urls import url
#from django.urls.resolvers import URLPattern
from resume_app import views

urlpatterns = [
    path('',views.index, name = 'index'),


]