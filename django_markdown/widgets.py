from django import forms
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.safestring import mark_safe


class MarkdownWidget(forms.Textarea):
    class Media:
        js = (
                settings.STATIC_URL + 'django_markdown/jquery.markitup.js',
                settings.STATIC_URL + 'django_markdown/markdown.js',
        )
        css = {
            'screen': (
                settings.STATIC_URL + 'django_markdown/skins/markitup/style.css',
                settings.STATIC_URL + 'django_markdown/markdown.css',
            )
        }

    def render(self, name, value, attrs=None):
        html = super(MarkdownWidget, self).render(name, value, attrs)

        html += ('<script type="text/javascript">'
                '(function($) { '
                'mySettings.previewParserPath = "%(path)s";'
                 '$(document).ready(function() {'
                 '  $("#%(id)s").markItUp(mySettings);'
                 '});'
                 '})(jQuery || django.jQuery);'
                 '</script>' % {'id': attrs['id'], 'path': reverse('django_markdown_preview') })
        return mark_safe(html)

