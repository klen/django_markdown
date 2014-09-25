""" Markdown utils. """
from django.core.urlresolvers import reverse
import markdown as markdown_module
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from django.template import loader, Context

try:
    import json as simplejson
except ImportError:
    try:
        import simplejson
    except ImportError:
        from django.utils import simplejson

from . import settings


def markdown(value, extensions=settings.MARKDOWN_EXTENSIONS,
             extension_configs=settings.MARKDOWN_EXTENSION_CONFIGS,
             safe=False):
    """ Render markdown over a given value, optionally using varios extensions.

    Default extensions could be defined which MARKDOWN_EXTENSIONS option.

    :returns: A rendered markdown

    """
    return mark_safe(markdown_module.markdown(
        force_text(value), extensions=extensions,
        extension_configs=extension_configs, safe_mode=safe))


def editor_js_initialization(selector, **extra_settings):
    """ Return script tag with initialization code. """

    INIT_TEMPLATE = loader.get_template(
        settings.MARKDOWN_EDITOR_INIT_TEMPLATE)

    options = dict(
        previewParserPath=reverse('django_markdown_preview'),
        **settings.MARKDOWN_EDITOR_SETTINGS)
    options.update(extra_settings)
    ctx = Context(dict(
        selector=selector, extra_settings=simplejson.dumps(options)),
        autoescape=False)
    return INIT_TEMPLATE.render(ctx)
