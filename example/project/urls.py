from django.urls import (include, path, re_path)

from django.contrib import admin
admin.autodiscover()

from django_markdown import flatpages
flatpages.register()

urlpatterns = [
    re_path(r'^markdown/', include('django_markdown.urls')),
    re_path(r'^admin/', include(admin.site.urls)),
    re_path(r'^pages/', include('django.contrib.flatpages.urls')),
    path(r'', include('project.md.urls')),
    ]
