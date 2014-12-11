from django.template import Library
from django.conf import settings

register = Library()

_static = None


def _is_installed(app):
    """Workaround for checking whether app is installed that is compatable with
    django 1.7 approach as well as providing backward compatability with
    versions <1.7
    """
    try:
        from django.apps import apps
    except ImportError:
        from django.conf import settings
        return app in settings.INSTALLED_APPS
    else:
        return apps.is_installed(app)

@register.simple_tag
def static(path):
    global _static
    if _static is None:
        if _is_installed('django.contrib.staticfiles'):
            from django.contrib.staticfiles.templatetags.staticfiles import static as _static
        else:
            from django.templatetags.static import static as _static
    return _static(path)
