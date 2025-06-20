"""
WSGI config for strum_and_strings project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

if os.path.exists("env.py"):
    import env

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'strum_and_strings.settings')

application = get_wsgi_application()
