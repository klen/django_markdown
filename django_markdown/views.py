""" Supports preview. """

from django.shortcuts import render

from . import settings


def preview(request):
    """ Render preview page.

    :returns: A rendered preview

    """
    return render(
        request, settings.MARKDOWN_PREVIEW_TEMPLATE, dict(
            content=request.REQUEST.get('data', 'No content posted'),
            css=settings.STATIC_URL + settings.MARKDOWN_STYLE,
        ))
