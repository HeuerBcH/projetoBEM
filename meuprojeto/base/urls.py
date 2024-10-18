from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('entrar/', views.entrar, name='entrar'),  # Define a página inicial como a página de login
    path('home/', views.home, name='home'),
    path('login/', views.login_user, name='login'),  # URL para a página de login
    path('cadastro/', views.cadastro_user, name='cadastro'),  # URL para a página de cadastro
    path('logout/', views.logout_user, name='logout'), # URL para logout
    path('entrar/', views.entrar, name='entrar'), # URL para pagina de entrada de usuario
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)