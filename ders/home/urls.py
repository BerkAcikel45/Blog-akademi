from django.urls import path

from home.views import homeView, about

urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('about', about, name='about')
]