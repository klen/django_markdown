from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'project.md.views.home'),
)
