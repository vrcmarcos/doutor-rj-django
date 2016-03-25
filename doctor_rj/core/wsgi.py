"""
WSGI config for doctor_where project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, "doctor_rj"))
sys.path.insert(1, os.path.join(PROJECT_ROOT, "doctor_rj/core"))
sys.path.insert(2, os.path.join(PROJECT_ROOT, "doctor_rj/doctor_rj"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_wsgi_application()
