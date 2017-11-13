""" Widgets for django-markdown. """
import os

from django import forms
from django.contrib.admin.widgets import AdminTextareaWidget
from django.core.files.storage import default_storage
from django.utils.safestring import mark_safe

from . import settings
from .utils import editor_js_initialization


class MarkdownWidget(forms.Textarea):

    """ Widget for a textarea.

    Takes two additional optional keyword arguments:

    ``markdown_set_name``
        Name for current set. Default: value of MARKDOWN_SET_NAME setting.

    ``markdown_skin``
        Name for current skin. Default: value of MARKDOWN_EDITOR_SKIN setting.

    """

    def render(self, name, value, attrs=None):
        """ Render widget.

        :returns: A rendered HTML

        """

        final_attrs = {'data-widget': 'markItUpEditor'}
        if attrs is not None:
            final_attrs.update(attrs)

        html = super(MarkdownWidget, self).render(name, value, final_attrs)
        final_attrs = self.build_attrs(final_attrs)
        html += editor_js_initialization("#%s" % attrs['id'])
        return mark_safe(html)

    class Media:
        css = {
            'screen': (
                os.path.join('django_markdown', 'skins', settings.MARKDOWN_EDITOR_SKIN, 'style.css'),
                os.path.join(settings.MARKDOWN_SET_PATH, settings.MARKDOWN_SET_NAME, 'style.css')
            )
        }

        js = (
            os.path.join('django_markdown', 'jquery.init.js'),
            os.path.join('django_markdown', 'jquery.markitup.js'),
            os.path.join(settings.MARKDOWN_SET_PATH, settings.MARKDOWN_SET_NAME, 'set.js')
        )


class AdminMarkdownWidget(MarkdownWidget, AdminTextareaWidget):

    """ Support markdown widget in Django Admin. """

    pass
