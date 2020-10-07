"""cas_client01 URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from simple_sso.sso_client.client import Client

test_client = Client(settings.SSO_SERVER, settings.SSO_PUBLIC_KEY, settings.SSO_PRIVATE_KEY)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/',
         test_client.login_view.as_view(client = test_client),
         name = 'simple-sso-login'),
    path('client/authenticate/',
         test_client.authenticate_view.as_view(client = test_client),
         name = 'simple-sso-authenticate'),
    path('', TemplateView.as_view(template_name = 'base.html'), name = 'home')
]
