from django.contrib import admin
from django.urls import path, include
from youtube import views

urlpatterns = [
    path('',views.youtube, name = 'youtube'),
    path('first/', views.first, name = 'first'),
    path('second/', views.second, name = 'second'),
]