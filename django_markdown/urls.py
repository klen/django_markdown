from django.conf.urls.defaults import url, patterns

from django_markdown.views import preview


urlpatterns = patterns( '',
        url('preview/$', preview, name='django_markdown_preview'),
    )
