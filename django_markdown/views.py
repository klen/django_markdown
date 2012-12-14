from django.shortcuts import render
from django.conf import settings


def preview(request):
    media_or_static = settings.STATIC_URL or settings.MEDIA_URL
    css = getattr(settings, 'DJANGO_MARKDOWN_STYLE', media_or_static + 'django_markdown/preview.css')

    return render(
        request, 'django_markdown/preview.html',
        content=request.REQUEST.get('data', 'No content posted'), css=css)
