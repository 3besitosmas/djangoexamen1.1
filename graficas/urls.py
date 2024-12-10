from django.contrib import admin
from django.urls import path
from . import views

 
urlpatterns = [
    path('',views.graficas_view, name= 'grafica_view'),
]