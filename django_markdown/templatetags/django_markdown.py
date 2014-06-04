""" Support 'markdown' filter. """
import posixpath

from django import template
from django.core.urlresolvers import reverse

from ..utils import markdown as _markdown, settings, simplejson, mark_safe


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
    extensions = (arg and arg.split(',')) or settings.MARKDOWN_EXTENSIONS
    return _markdown(value, extensions=extensions, safe=False)


@register.filter(is_safe=True)
def markdown_safe(value, arg=None):
    """ Render markdown over a given value, optionally using varios extensions.

    Default extensions could be defined which MARKDOWN_EXTENSIONS option.

    Enables safe mode, which strips raw HTML and only returns HTML generated
    by markdown.

    :returns: A rendered markdown.

    """
    extensions = (arg and arg.split(',')) or settings.MARKDOWN_EXTENSIONS
    return _markdown(value, extensions=extensions, safe=True)


@register.inclusion_tag('django_markdown/editor_init.html')
def markdown_editor(selector):
    """ Enable markdown editor for given textarea.

    :returns: Editor template context.

    """
    return dict(
        selector=selector,
        extra_settings=mark_safe(simplejson.dumps(
            dict(previewParserPath=reverse('django_markdown_preview')))))


@register.inclusion_tag('django_markdown/media_all.html')
def markdown_media():
    """ Add css and js requirements to HTML.

    :returns: Editor template context.

    """
    ctx = markdown_media_js()
    ctx.update(markdown_media_css())
    return ctx


@register.inclusion_tag('django_markdown/media_js.html')
def markdown_media_js():
    """ Add js requirements to HTML.

    :returns: Editor template context.

    """
    return dict(
        JS_SET=posixpath.join(
            settings.MARKDOWN_SET_PATH, settings.MARKDOWN_SET_NAME, 'set.js'
        )
    )


@register.inclusion_tag('django_markdown/media_css.html')
def markdown_media_css():
    """ Add css requirements to HTML.

    :returns: Editor template context.

    """
    return dict(
        CSS_SET=posixpath.join(
            settings.MARKDOWN_SET_PATH, settings.MARKDOWN_SET_NAME, 'style.css'
        ),
        CSS_SKIN=posixpath.join(
            'django_markdown', 'skins', settings.MARKDOWN_EDITOR_SKIN,
            'style.css'
        )
    )
