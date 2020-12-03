"""python_for_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.index),

    path('firstapp/business', views.business, name='business'),
    path('firstapp/business-ua', views.business_ua, name='business_ua'),
    path('firstapp/creative', views.creative, name='creative'),
    path('firstapp/creative-ua', views.creative_ua, name='creative_ua'),

    path('secondapp/regex', views.regex, name='regex'),
]
