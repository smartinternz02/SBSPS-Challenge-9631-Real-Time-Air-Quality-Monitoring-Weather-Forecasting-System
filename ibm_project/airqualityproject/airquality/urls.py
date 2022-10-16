from django.contrib import admin
from django.urls import path
from airqualityapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path(r'weather/',views.weather,name='weather'),
    path(r'Air/',views.Air,name='Air'),
    path('Airout/',views.Airout,name= 'Airout'),
    path(r'about/',views.about,name='about'),
    path(r'contact/',views.contact,name = 'contact'),
]
