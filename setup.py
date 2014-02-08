import os

from setuptools import setup, find_packages

from django_markdown import version, PROJECT, LICENSE


MODULE_NAME = 'django_markdown'
PACKAGE_DATA = list()

for directory in ['templates', 'static']:
    for root, dirs, files in os.walk(os.path.join(MODULE_NAME, directory)):
        for filename in files:
            PACKAGE_DATA.append("%s/%s" %
                                (root[len(MODULE_NAME) + 1:], filename))


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

install_requires = [l for l in read('requirements.txt').split('\n')
                    if l and not l.startswith('#')]

META_DATA = dict(
    name=PROJECT,
    version=version,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license=LICENSE,

    author="Kirill Klenov",
    author_email="horneds@gmail.com",
    url="http://github.com/klen/django-markdown.git",

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
    tests_require=install_requires,
    test_suite='tests',
)

if __name__ == "__main__":
    setup(**META_DATA)
