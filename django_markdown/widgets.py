""" Widgets for django-markdown. """
import posixpath

from django import forms
from django.contrib.admin.widgets import AdminTextareaWidget
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

    def __init__(self, attrs=None, markdown_set_name=None, markdown_skin=None):
        self.__set = markdown_set_name or settings.MARKDOWN_SET_NAME
        self.__skin = markdown_skin or settings.MARKDOWN_EDITOR_SKIN
        super(MarkdownWidget, self).__init__(attrs)

    @property
    def media(self):
        """ Prepare media files.

        :returns: form's media

        """

        js = (
            posixpath.join(settings.STATIC_URL, 'django_markdown', 'jquery.init.js'), # noqa
            posixpath.join(settings.STATIC_URL, 'django_markdown', 'jquery.markitup.js'), # noqa
            posixpath.join(settings.STATIC_URL, settings.MARKDOWN_SET_PATH, self.__set, 'set.js'), # noqa
        )
        css = {
            'screen': (
                posixpath.join(settings.STATIC_URL, 'django_markdown', 'skins', self.__skin, 'style.css'), # noqa
                posixpath.join(settings.STATIC_URL, settings.MARKDOWN_SET_PATH, self.__set, 'style.css'), # noqa
            )
        }
        return forms.Media(css=css, js=js)

    def render(self, name, value, attrs=None):
        """ Render widget.

        :returns: A rendered HTML

        """
        html = super(MarkdownWidget, self).render(name, value, attrs)
        attrs = self.build_attrs(attrs)
        html += editor_js_initialization("#%s" % attrs['id'])
        return mark_safe(html)


class AdminMarkdownWidget(MarkdownWidget, AdminTextareaWidget):

    """ Support markdown widget in Django Admin. """

    pass
