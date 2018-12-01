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
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('palm/', include("palm.urls")),
    path('data/', include("data.urls")),
    path('accounts/', include('accounts.urls')),
    path('social-account', include('allauth.urls')), # allauth.urls 에 대한 지정을 해주어야 소셜 acess token에 대한 rest_framework token을 반환해준다 존나힘드네 ;;
    path('test_app/', include('test_app.urls')),
    path('accounts/login/', auth_views.login, name = 'login', kwargs = {'template_name' : 'login.html'}),
    path('accounts/logout/', auth_views.logout, name = 'logout', kwargs = {'next_page':settings.LOGIN_URL,}),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-jwt-auth/', obtain_jwt_token),
    path('api-jwt-auth/refresh/', refresh_jwt_token),
    path('api-jwt-auth/verify/', verify_jwt_token),
    path('test_api/', include('test_api.urls', namespace='test_api')),
    path('api-token-auth/', obtain_auth_token),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # etc
]
