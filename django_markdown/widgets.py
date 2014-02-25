""" Widgets for django-markdown. """
from django import forms
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminTextareaWidget

from . import settings


try:
    import json as simplejson
except ImportError:
    try:
        import simplejson
    except ImportError:
        from django.utils import simplejson


class MarkdownWidget(forms.Textarea):

    """ Widget for a textarea. """

    class Media(object):

        """ Widget's media files. """

        js = (
            settings.STATIC_URL + 'django_markdown/jquery.init.js',
            settings.STATIC_URL + 'django_markdown/jquery.markitup.js',
            settings.STATIC_URL + 'django_markdown/markdown.js',
        )
        css = {
            'screen': (
                settings.STATIC_URL + 'django_markdown/skins/%s/style.css' % settings.MARKDOWN_EDITOR_SKIN, # noqa
                settings.STATIC_URL + 'django_markdown/markdown.css',
            )
        }

    def render(self, name, value, attrs=None):
        """ Render widget.

        :returns: A rendered HTML

        """
        html = super(MarkdownWidget, self).render(name, value, attrs)

        editor_settings = settings.MARKDOWN_EDITOR_SETTINGS
        editor_settings['previewParserPath'] = reverse(
            'django_markdown_preview')

        html += '<script type="text/javascript">miu.init("%s", %s)</script>' % ( # noqa
            attrs['id'], simplejson.dumps(editor_settings))

        return mark_safe(html)


class AdminMarkdownWidget(MarkdownWidget, AdminTextareaWidget):

    """ Support markdown widget in Django Admin. """

    pass
