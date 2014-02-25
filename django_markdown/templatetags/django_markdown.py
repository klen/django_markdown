""" Support 'markdown' filter. """
import markdown as markdown_module
from django import template
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

from ..settings import MARKDOWN_EXTENSIONS


register = template.Library()


@register.filter(is_safe=True)
def markdown(value):
    """ Render markdown.

    :returns: A rendered string

    """
    return mark_safe(markdown_module.markdown(
        force_text(value), extensions=MARKDOWN_EXTENSIONS, safe_mode=False))


@register.filter(is_safe=True)
def markdown_safe(value):
    """ Safe Rendering markdown.

    :returns: A rendered string.

    """
    return mark_safe(markdown_module.markdown(
        force_text(value), extensions=MARKDOWN_EXTENSIONS, safe_mode=True))
