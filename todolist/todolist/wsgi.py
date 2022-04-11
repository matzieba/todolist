"""
WSGI config for todolist project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
sys.path.append('C:\Users\Mati\Desktop\dev\protfolio 100doc\todolist')
sys.path.append('C:\Users\Mati\Desktop\dev\protfolio 100doc\todolist\todolist')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todolist.settings')

application = get_wsgi_application()
