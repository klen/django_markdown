import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')

from django.core.management import call_command
call_command('syncdb', interactive=False)

from django_markdown.tests import *
