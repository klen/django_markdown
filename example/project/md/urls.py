from django.urls import re_path

urlpatterns = [
    re_path(r'^$', 'project.md.views.home'),
]
