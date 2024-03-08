"""
WSGI config for tst_5f21a634_f7af_461_153 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "tst_5f21a634_f7af_461_153.settings"
)

application = get_wsgi_application()
