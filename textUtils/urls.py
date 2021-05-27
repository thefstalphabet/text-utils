"""textUtils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

# connected views.py file on this file
from . import views

urlpatterns = [
    # this code/path is for IP address of our projects
    path('admin/', admin.site.urls),

    # this code/path is for index page, here we created path of index pages
    path('', views.index, name='index'),

    # this code/path is for analyzed page, here we created path of analyzed pages
    path('analyzed', views.analyzed, name='analyzed'),

    # this code/path is for contact us page, here we created path of contact us pages
    path('contactus', views.contactus, name='contactus'),

    # this code/path is for about us page, here we created path of contact us pages
    path('aboutus', views.aboutus, name='aboutus'),
]
