from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('music/', views.music, name='music'),
    path('performances/', views.performances, name='performances'),
    path('contact/', views.contact, name='contact'),
]
