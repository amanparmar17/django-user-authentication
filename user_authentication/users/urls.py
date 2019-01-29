from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.index,name='index'),
    path('register', views.register,name='register'),
]