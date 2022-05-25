from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard/generatefromfile/', views.GenerateFromFileView.as_view(), name='generatefromfile'),
]