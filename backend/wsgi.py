"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application
import urllib.request

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

if not settings.DEBUG:
    # Retrive the index file from the CDN in production
    index = 'index.html'
    urllib.request.urlretrieve(
        os.environ['PARROT_CDN_HOST'] + '/' + index,
        'static/' + index)

application = get_wsgi_application()
