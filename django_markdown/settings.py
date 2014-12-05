""" Application settings. """

from django.conf import settings


MARKDOWN_EDITOR_INIT_TEMPLATE = getattr(settings, 'MARKDOWN_EDITOR_INIT_TEMPLATE', 'django_markdown/editor_init.html')
MARKDOWN_EDITOR_SETTINGS = getattr(settings, 'MARKDOWN_EDITOR_SETTINGS', {})
MARKDOWN_EDITOR_SKIN = getattr(settings, 'MARKDOWN_EDITOR_SKIN', 'simple')
MARKDOWN_EXTENSIONS = getattr(settings, 'MARKDOWN_EXTENSIONS', [])
MARKDOWN_EXTENSION_CONFIGS = getattr(settings, 'MARKDOWN_EXTENSION_CONFIGS', {})
MARKDOWN_SET_PATH = getattr(settings, 'MARKDOWN_SET_PATH', 'django_markdown/sets')
MARKDOWN_SET_NAME = getattr(
    settings, 'MARKDOWN_SET_NAME',
    'markdownextra' if 'extra' in MARKDOWN_EXTENSIONS else 'markdown')

MARKDOWN_PREVIEW_TEMPLATE = getattr(settings, 'MARKDOWN_PREVIEW_TEMPLATE', 'django_markdown/preview.html')
MARKDOWN_STYLE = getattr(settings, 'MARKDOWN_STYLE', 'django_markdown/preview.css')
MARKDOWN_PROTECT_PREVIEW = getattr(settings, 'MARKDOWN_PROTECT_PREVIEW', False)

LOGIN_URL = settings.LOGIN_URL
