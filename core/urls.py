from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('' ,views.index),
    path('getdata', views.getData),
    path('data/<str:slug>' , views.specificData)
]
