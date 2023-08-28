"""
URL configuration for meeting_planner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path

""" 
My Notes
I imported the app I built called website - add to URLs page
I also added this to the urlpatterns list read as when I go to welcome html, run the welcome function

My notes
To make welcome the default page of the site, instead of welcome.html, we can write path 
as path('', welcome) in the below


"""

from website.views import welcome,date, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome.html', welcome),
    path('date', date),
    path('about', about),
]
