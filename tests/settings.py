""" Settings for tests. """

import tempfile

TMPDIR = tempfile.mkdtemp()

ROOT_URLCONF = 'tests.urls'

SECRET_KEY = 'KeepMeSecret'

DEBUG = True

MEDIA_ROOT = TMPDIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'TEST_CHARSET': 'utf8',
    }
}

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django_markdown',
    'tests',
)
