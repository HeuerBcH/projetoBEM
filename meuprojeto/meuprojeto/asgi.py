## Tanto o arquivo asgi.py quanto o arquivo wsgi.py são arquivos que possuem as configurações que passam instruções para servidores,
## para quando aplicarmos o site dentro de um servidor, o servidor saber como operar (existem servidores do tipo asgi e wsgi)

"""
ASGI config for meuprojeto project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meuprojeto.settings')

application = get_asgi_application()
