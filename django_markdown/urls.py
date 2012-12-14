from django.conf.urls import patterns, url

from django_markdown.views import preview


urlpatterns = patterns( '',
        url('preview/$', preview, name='django_markdown_preview'),
    )
