#!/usr/bin/env python
# coding: utf-8
import os

from django.core.management import call_command
from django.conf.urls import patterns, include
from django.conf import settings
from django.http import HttpResponse


MODULE, _ = os.path.splitext(os.path.basename(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", MODULE)


# Settings
# --------
DEBUG=True,
ROOT_URLCONF=MODULE
SECRET_KEY='secret'
INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.auth',
    'django.contrib.admin',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
)

if not settings.configured:
    settings.configure(**locals())


# Models
# ------
from django.db import models

from django_markdown.models import MarkdownField

class Test(models.Model):
    content = MarkdownField()

    class Meta:
        app_label = 'test'


# Views
# -----
def home(request):
    return HttpResponse('OK')


# Urls
# ----
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns(
    '',
    ('^$', home),
    ('^admin/', include(admin.site.urls)),
)


if __name__ == '__main__':
    call_command('runserver')
