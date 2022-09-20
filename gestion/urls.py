"""gestion URL Configuration

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
from django.urls import path, include
from gestion.views import inicio
from administrador.views import inicioadmin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('inicio-ad/', inicioadmin, name="inicioadmin"),
    path('', include('administrador.urls')),
    path('', include('usuarios.urls')),
    path('', include('facturas.urls')),
    # Logueo
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='usuario-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='usuario-logout'),
    # Recuperación
    path('password_reset/', 
        auth_views.PasswordResetView.as_view(template_name='recuperacion/password_reset.html', email_template_name='recuperacion/password_reset_email.html'),
        name='password_reset'),
    path('password_reset_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name='recuperacion/password_reset_sent.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='recuperacion/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password_reset_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='recuperacion/password_reset_complete.html'),
        name='password_reset_complete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
