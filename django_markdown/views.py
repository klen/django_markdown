""" Supports preview. """
from django.core.files.storage import default_storage
from django.shortcuts import render

from . import settings


def preview(request):
    """ Render preview page.

    :returns: A rendered preview

    """
    if settings.MARKDOWN_PROTECT_PREVIEW:
        user = getattr(request, 'user', None)
        if not user or not user.is_staff:
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(request.get_full_path())

    # https://github.com/klen/django_markdown/pull/60
    if request.POST:
        content = request.POST.get('data', 'No content posted.')
    else:
        content = request.REQUEST.get('data', 'No content posted.')

    return render(
        request, settings.MARKDOWN_PREVIEW_TEMPLATE, dict(
            content=content,
            css=settings.MARKDOWN_STYLE
        ))
