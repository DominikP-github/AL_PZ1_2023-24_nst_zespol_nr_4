"""
URL configuration for projekt2 project.

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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/', views.Main, name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('search_history_detail/<int:history_id>/', views.search_history_detail, name='search_history_detail'),
    path('delete_history/<int:history_id>/', views.delete_history, name='delete_history'),
    path('special_page/', views.display_forms, name='special_page'),
    path('form/', views.form_page, name='form_page'),
    path('success/', views.success_page, name='success_page'),
    path('delete-form/<int:form_id>/', views.delete_form, name='delete_form'),
    path('change_credentials/', views.change_credentials, name='change_credentials'),
]
