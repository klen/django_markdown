from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

def preview(request):
    media_or_static = settings.STATIC_URL or settings.MEDIA_URL
    css = getattr(settings, 'DJANGO_MARKDOWN_STYLE', media_or_static + 'django_markdown/preview.css')
    content=request.REQUEST.get('data', 'No content posted')
    return  render_to_response('django_markdown/preview.html', locals(), context_instance=RequestContext(request))
