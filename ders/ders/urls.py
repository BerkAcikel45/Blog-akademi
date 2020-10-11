"""ders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.shortcuts import render
from django.urls import path, include
from django.http import HttpResponse

def about1(request):
    print(request)
    print("asassda")
    return render(request, 'about.html',
   {'hello': 'Hello World!', 'array': [1, 2, 3, 4, 5]})


def index(request):
    return render(request, 'index.html',
     {'user_name': 'Berk Açıkel',
     'welcome_message': 'Berk Hoşgeldin'})


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('home.urls')),

    path('about/', about1, name='about1'),
    path('index/', index, name='index')
]
