""" Define preview URL. """

from django import VERSION
from django.conf.urls import url

from .views import preview


if VERSION >= (1, 8):
    urlpatterns = [
        url('preview/$', preview, name='django_markdown_preview')
    ]
else:
    # django <= 1.7 compatibility
    from django.conf.urls import patterns
    urlpatterns = patterns(
        '', url('preview/$', preview, name='django_markdown_preview')
    )
