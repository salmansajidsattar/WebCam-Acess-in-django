from django.contrib import admin
from django.urls import path,include
from web import views

urlpatterns = [
    path('',views.index),
    path('VidFeed/',views.VidFeed,name='VidFeed')
]