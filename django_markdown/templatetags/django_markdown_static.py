from django.template import Library
from django.conf import settings

register = Library()

_static = None


@register.simple_tag
def static(path):
    global _static
    if _static is None:
        if 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
            from django.contrib.staticfiles.templatetags.staticfiles import static as _static
        else:
            from django.templatetags.static import static as _static
    return _static(path)
