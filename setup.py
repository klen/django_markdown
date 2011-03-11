import os

from setuptools import setup, find_packages

from django_markdown import VERSION, PROJECT, LICENSE


MODULE_NAME = 'django_markdown'
PACKAGE_DATA = list()

for directory in [ 'templates', 'static' ]:
    for root, dirs, files in os.walk( os.path.join( MODULE_NAME, directory )):
        for filename in files:
            PACKAGE_DATA.append("%s/%s" % ( root[len(MODULE_NAME)+1:], filename ))


def read( fname ):
    try:
        return open( os.path.join( os.path.dirname( __file__ ), fname ) ).read()
    except IOError:
        return ''


META_DATA = dict(
    name = PROJECT,
    version = VERSION,
    description = read('DESCRIPTION'),
    long_description = read('README.rst'),
    license=LICENSE,

    author = "Kirill Klenov",
    author_email = "horneds@gmail.com",
    url = "http://github.com/klen/django-markdown.git",

    keywords= 'html markdown django',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Text Processing :: Markup',
    ],

    packages = find_packages(),
    package_data = { '': PACKAGE_DATA, },

    install_requires = [ 'markdown' ],
)

if __name__ == "__main__":
    setup( **META_DATA )
