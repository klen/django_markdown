from django.conf.urls import include, url

urlpatterns = [
    url(r'^markdown/', include('django_markdown.urls')),
]
