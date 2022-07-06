"""Ami URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Ami import views
from Ami.views import home_view



  
urlpatterns = [
    #Swelcome  font page path
    path("w",views.welcome),
    #admin page
    # path('rohit/', admin.site.urls),
    # First page path
    path("1",views.fpage),
    #Secound page path
    path("2",views.spage),
    #third page path
    path("3",views.tpage),
    #fout page  page path
    path("4",views.fourpage),
    #rish page to
    path("q",views.RichHome),
    path("a",views.home_view)    
]


