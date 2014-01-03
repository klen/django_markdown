""" Support 'markdown' filter. """

import markdown as mkdn

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def markdown(value):
    """ Render markdown.

    :returns: A rendered string

    """
    return mark_safe(mkdn.markdown(value, safe_mode='escape'))
