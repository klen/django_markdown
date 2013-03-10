from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.utils import simplejson


class MarkdownWidget(forms.Textarea):
    class Media:
        js = (
            ( settings.STATIC_URL or settings.MEDIA_URL ) + 'django_markdown/jquery.min.js',
            ( settings.STATIC_URL or settings.MEDIA_URL ) + 'django_markdown/jquery.markitup.js',
            ( settings.STATIC_URL or settings.MEDIA_URL ) + 'django_markdown/sets/markdown/set.js',

        )
        css = {
            'screen': (
                ( settings.STATIC_URL or settings.MEDIA_URL ) + 'django_markdown/skins/%s/style.css' % getattr(settings,
                                                                                                               'MARKDOWN_EDITOR_SKIN',
                                                                                                               'simple'),
                ( settings.STATIC_URL or settings.MEDIA_URL ) + 'django_markdown/sets/markdown/style.css',
                ( settings.STATIC_URL or settings.MEDIA_URL ) + 'django_markdown/style.css',
            )
        }

    def render(self, name, value, attrs=None):
        html = super(MarkdownWidget, self).render(name, value, attrs)

        editor_settings = getattr(settings, 'MARKDOWN_EDITOR_SETTINGS', {})
        editor_settings['previewParserPath'] = reverse('django_markdown_preview')

        html += "<script type='text/javascript'>$('#%s').markItUp($.extend(mySettings,%s));</script>" % (
        attrs['id'], simplejson.dumps(editor_settings))
        #html += '<script type="text/javascript">miu.init(\'%s\', %s)</script>' % (attrs['id'], simplejson.dumps(editor_settings))

        return mark_safe(html)


