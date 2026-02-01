from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.registerView, name='register'),
    path('home/', views.homeView, name='createshorturl'),
    path('login/', views.loginView, name ='login'),
    path('logout/', views.logoutUser, name='logout'),
]
