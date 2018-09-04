""" Define preview URL. """

from django.conf.urls import *

from .views import preview

urlpatterns = patterns(
    '', url('preview/$', preview, name='django_markdown_preview'))
