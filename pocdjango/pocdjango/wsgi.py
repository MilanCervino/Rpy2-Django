"""
WSGI config for pocdjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pocdjango.settings')
#os.environ['R_HOME']='C:/Program Files/R/R-4.1.3'

application = get_wsgi_application()
