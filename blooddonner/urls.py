"""blooddonner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.views.generic import RedirectView
import blooddonner.settings as settings
from django.contrib.auth.views import LogoutView
from bldapp.views import Authentication

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bloodDonner/', include('bldapp.urls')),
    path('', RedirectView.as_view(url='/bloodDonner/', permanent=True)),
    path('login/', Authentication.login, name="login"),
    path('registration/', Authentication.register, name="registration"),  
    path('logout/', LogoutView.as_view(next_page = settings.LOGOUT_REDIRECT_URL), name="logout"),
]
