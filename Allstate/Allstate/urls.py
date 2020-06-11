"""Allstate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from insurance.views import register, home, add_customer, view_customers, update_customer, delete_customer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='insurance/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='insurance/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('add_customer/', add_customer, name='add_customer'),
    path('view_customers/', view_customers, name='view_customers'),
    path('update_customer/<str:name>', update_customer, name='update_customer'),
	path('delete_customer/<str:cname>', delete_customer, name='delete_customer'),
    path('', home, name='home'),
]
