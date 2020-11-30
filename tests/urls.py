from django.urls import (include, re_path)

urlpatterns = [
    re_path(r'^markdown/', include('django_markdown.urls')),
]
