""" Application settings. """

import posixpath

from django.conf import settings


MARKDOWN_EDITOR_SETTINGS = getattr(settings, 'MARKDOWN_EDITOR_SETTINGS', {})
MARKDOWN_EDITOR_SKIN = getattr(settings, 'MARKDOWN_EDITOR_SKIN', 'simple')
MARKDOWN_EXTENSIONS = getattr(settings, 'MARKDOWN_EXTENSIONS', [])
MARKDOWN_SET_PATH = getattr(settings, 'MARKDOWN_SET_PATH', posixpath.join(
    'django_markdown', 'sets'
))
MARKDOWN_SET_NAME = getattr(
    settings, 'MARKDOWN_SET_NAME',
    'markdownextra' if 'extra' in MARKDOWN_EXTENSIONS else 'markdown')

MARKDOWN_STYLE = getattr(settings, 'MARKDOWN_STYLE', posixpath.join(
    'django_markdown', 'preview.css'
))
STATIC_URL = settings.STATIC_URL or settings.MEDIA_URL
