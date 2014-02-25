""" Supports preview. """

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .settings import MARKDOWN_STYLE, STATIC_URL


@csrf_exempt
def preview(request):
    """ Render preview page.

    :returns: A rendered preview

    """
    return render(
        request,
        'django_markdown/preview.html', dict(
            content=request.REQUEST.get('data', 'No content posted'),
            css=STATIC_URL + MARKDOWN_STYLE
        ))
