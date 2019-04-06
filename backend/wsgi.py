"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# We need to import retrieve_index_file after loading the settings
# pylint: disable=wrong-import-position
from .retrieve_index_file import retrieve_index_file

retrieve_index_file()
application = get_wsgi_application()
