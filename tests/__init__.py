import os

from django import VERSION
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')


if VERSION >= (1, 7):
    from django.conf import settings
    from django.apps import apps

    apps.populate(settings.INSTALLED_APPS)
    call_command('migrate', interactive=False)
else:
    call_command('syncdb', interactive=False)

from django_markdown.tests import *  # noqa
