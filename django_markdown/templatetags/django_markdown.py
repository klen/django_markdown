""" Support 'markdown' filter. """
from django import template

from ..utils import markdown as _markdown, MARKDOWN_EXTENSIONS


register = template.Library()


@register.filter(is_safe=True)
def markdown(value, arg=None):
    """ Render markdown over a given value, optionally using varios extensions.

    Default extensions could be defined which MARKDOWN_EXTENSIONS option.

    Syntax: ::

        {{value|markdown}}

        {{value|markdown:"tables,codehilite"}}

    :returns: A rendered markdown

    """
    extensions = (arg and arg.split(',')) or MARKDOWN_EXTENSIONS
    return _markdown(value, extensions=extensions, safe=False)


@register.filter(is_safe=True)
def markdown_safe(value, arg=None):
    """ Render markdown over a given value, optionally using varios extensions.

    Default extensions could be defined which MARKDOWN_EXTENSIONS option.

    Enables safe mode, which strips raw HTML and only returns HTML generated
    by markdown.

    :returns: A rendered markdown.

    """
    extensions = (arg and arg.split(',')) or MARKDOWN_EXTENSIONS
    return _markdown(value, extensions=extensions, safe=True)
