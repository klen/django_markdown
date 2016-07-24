from django import VERSION
from django.conf.urls import include, url

if VERSION >= (1, 8):
    urlpatterns  = [
        url(r'^markdown/', include('django_markdown.urls')),
    ]
else:
    # django <= 1.7.*
    from django.conf.urls import patterns
    urlpatterns = patterns(
        '',
        (r'^markdown/', include('django_markdown.urls')),
    )
