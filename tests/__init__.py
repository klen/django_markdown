import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')

from django import VERSION

if VERSION >= (1, 7):
    from django.conf import settings
    from django.apps import apps

    apps.populate(settings.INSTALLED_APPS)

from django.core.management import call_command
call_command('syncdb', interactive=False)

from django_markdown.tests import * # noqa
