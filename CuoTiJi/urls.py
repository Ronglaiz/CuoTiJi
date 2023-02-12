"""CuoTiJi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from CuoTeJe import views
urlpatterns = [
    path('', views.main_page),
    path('main_page', views.main_page),
    path('insert_data_page', views.insert_data_page),
    path('query_data_page', views.query_data_page),

    path('insert_data', views.insert_data),
    path('query_data', views.query_data),
]
