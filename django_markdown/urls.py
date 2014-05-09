""" Define preview URL. """

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import user_passes_test

from django_markdown.views import preview

staff_required = user_passes_test(lambda user: user.is_staff)

urlpatterns = patterns(
    '', url('preview/$', staff_required(preview), name='django_markdown_preview'))
