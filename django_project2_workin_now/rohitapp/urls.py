from django.contrib import admin
from django.urls import path
from rohitapp import views


urlpatterns = [
    path('ami/',views.index)
    
]