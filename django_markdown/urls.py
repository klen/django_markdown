""" Define preview URL. """

from django.conf.urls import url

from .views import preview

urlpatterns = [
    url(r'^preview/$', preview, name='django_markdown_preview')]
