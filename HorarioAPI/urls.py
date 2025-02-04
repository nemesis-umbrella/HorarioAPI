"""HorarioAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from HorarioAPI.settings import LOGOUT_REDIRECT_URL
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from asistencia.views import index
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LogoutView

urlpatterns = [
    path('', index,name='index'),
    path('admin/', admin.site.urls),
    path('api/1.0/',include(('api.urls','api'))),
    path('asistencia/',include(('asistencia.urls','asistencia'))),
    path('api_generate_token/',views.obtain_auth_token),
    # Corresponde a las opciones de inicio de sesión 
    path('accounts/login/',LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=LOGOUT_REDIRECT_URL), name='logout'),
    path('reset/password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('reset/password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
