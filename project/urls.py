from django.urls import path
from . import views


urlpatterns = [
    path('', views.project, name='main'),
    path('contact/', views.contact, name='contact'),
    path('history/', views.history, name='history'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('iceland/', views.iceland, name='iceland'),
]