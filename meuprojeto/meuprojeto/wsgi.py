## Tanto o arquivo asgi.py quanto o arquivo wsgi.py são arquivos que possuem as configurações que passam instruções para servidores,
## para quando aplicarmos o site dentro de um servidor, o servidor saber como operar (existem servidores do tipo asgi e wsgi)

"""
WSGI config for meuprojeto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meuprojeto.settings')

application = get_wsgi_application()
