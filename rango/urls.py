from django.contrib import admin
from django.urls import path
from rango import views

urlpatterns = [
    path("", views.index, name='rango.index'),
    path(r'about/', views.about, name='rango.about'),

]
