from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('name/', views.name, name='name'),
    path('groupe/', views.groupe, name='groupe'),
    path('age/', views.age, name='age'),
    path('common/', views.common, name='common'),
]