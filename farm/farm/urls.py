"""farm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('palm/', include("palm.urls")),
    path('data/', include("data.urls")),
    path('accounts/', include('accounts.urls')),
    path('test_app/', include('test_app.urls')),
    path('accounts/login/', auth_views.login, name = 'login', kwargs = {'template_name' : 'login.html'}),
    path('accounts/logout/', auth_views.logout, name = 'logout', kwargs = {'next_page':settings.LOGIN_URL,})
    # etc
]
