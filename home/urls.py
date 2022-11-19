from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('course', views.course, name='course'),
    path('contact', views.contact, name='contact'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('singup', views.singup, name='singup'),
    # path('doremon', views.doremon, name='doremon')
]