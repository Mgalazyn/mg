from django.urls import path

from . import views

urlpatterns = [
    path('', views.project, name='main'),
    path('contact/', views.contact, name='contact'),
]