""" Setup Django-Markdown. """

import os

from setuptools import setup, find_packages
import re


MODULE_NAME = 'django_markdown'
PACKAGE_DATA = list()

for directory in ['templates', 'static']:
    for root, dirs, files in os.walk(os.path.join(MODULE_NAME, directory)):
        for filename in files:
            PACKAGE_DATA.append("%s/%s" %
                                (root[len(MODULE_NAME) + 1:], filename))


def _read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

_meta = _read('django_markdown/__init__.py')
_license = re.search(r'^__license__\s*=\s*"(.*)"', _meta, re.M).group(1)
_project = re.search(r'^__project__\s*=\s*"(.*)"', _meta, re.M).group(1)
_version = re.search(r'^__version__\s*=\s*"(.*)"', _meta, re.M).group(1)

install_requires = [l for l in _read('requirements.txt').split('\n')
                    if l and not l.startswith('#')]

setup(
    name=_project,
    version=_version,
    description=_read('DESCRIPTION'),
    long_description=_read('README.rst'),
    license=_license,

    author="Kirill Klenov",
    author_email="horneds@gmail.com",
    url="https://github.com/klen/django_markdown",

    keywords='html markdown django',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', # noqa
        'Programming Language :: Python',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Text Processing :: Markup',
    ],

    packages=find_packages(),
    package_data={'': PACKAGE_DATA, },

    install_requires=install_requires,
)

# pylama:ignore=C0111
