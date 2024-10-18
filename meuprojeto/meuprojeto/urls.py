from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='base/entrar/', permanent=False)), # Redireciona a raiz para a página de login, ou seja, a primeira pagina de acesso sera a de login
    path('base/', include('base.urls')),  # Inclui as URLs do app 'base'
    path('turma/', include('turma.urls')),  # Inclui as URLs do app turma
    path('simulado/', include('simulado.urls')),
    path('aluno/', include('aluno.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
