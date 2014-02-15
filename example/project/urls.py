from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django_markdown import flatpages
flatpages.register()

urlpatterns = patterns('',
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'', include('project.md.urls')),
)
