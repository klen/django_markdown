""" Support 'markdown' filter. """

from django import template
from django.utils.safestring import mark_safe
from django.utils.encoding import force_text

import markdown as markdown_module


register = template.Library()


@register.filter(is_safe=True)
def markdown(value):
    """ Render markdown.

    :returns: A rendered string

    """
    return mark_safe(
        markdown_module.markdown(force_text(value), safe_mode=False))


@register.filter(is_safe=True)
def markdown_safe(value):
    """ Safe Rendering markdown.

    :returns: A rendered string.

    """
    return mark_safe(
        markdown_module.markdown(force_text(value), safe_mode=True))
