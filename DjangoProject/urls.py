"""
URL configuration for DjangoProject project.

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
from FirstApp import views

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", views.Home, name="home"),
    path("home/", views.Home, name="home"),
    path("login/", views.Login, name="login"),
    path("signup/", views.Signup, name="signup"),
    path("forgetpassword/", views.ForgetPassword, name="forgetpassword"),
    path("app/", views.App, name="app"),
    path("showusers/", views.ShowUsers, name="showusers")
]
