from django import template
from django.templatetags.static import static as _static

register = template.Library()


@register.simple_tag
def static(path):
    return _static(path)
