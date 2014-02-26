""" Markdown utils. """
import markdown as markdown_module
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

from .settings import MARKDOWN_EXTENSIONS


def markdown(value, extensions=MARKDOWN_EXTENSIONS, safe=False):
    """ Render markdown over a given value, optionally using varios extensions.

    Default extensions could be defined which MARKDOWN_EXTENSIONS option.

    :returns: A rendered markdown

    """
    return mark_safe(markdown_module.markdown(
        force_text(value), extensions=extensions, safe_mode=safe))
