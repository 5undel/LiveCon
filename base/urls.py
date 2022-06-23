from django.contrib import admin
from django.urls import path
from . import views


# url path to the home page
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
]