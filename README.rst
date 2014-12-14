Django-Markdown v. 0.8.4
########################

.. _description:

**Django markdown** is django application that allows use markdown wysiwyg in flatpages, admin forms and other forms.
Documentaton available at pypi_ or github_.

.. _badges:

.. image:: http://img.shields.io/travis/klen/django_markdown.svg?style=flat-square
    :target: http://travis-ci.org/klen/django_markdown
    :alt: Build Status

.. image:: http://img.shields.io/coveralls/klen/django_markdown.svg?style=flat-square
    :target: https://coveralls.io/r/klen/django_markdown
    :alt: Coverals

.. image:: http://img.shields.io/pypi/v/django_markdown.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django_markdown
    :alt: Version

.. image:: http://img.shields.io/pypi/dm/django_markdown.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django_markdown
    :alt: Downloads

.. image:: http://img.shields.io/pypi/l/django_markdown.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django_markdown
    :alt: License

.. image:: http://img.shields.io/gratipay/klen.svg?style=flat-square
    :target: https://www.gratipay.com/klen/
    :alt: Donate

.. contents::

.. _requirements:

Requirements
============

- python >= 2.7
- django >= 1.6
- markdown


.. _installation:

Installation
============

**Django markdown** should be installed using pip: ::

    pip install django-markdown


Setup
=====

.. note:: 'django_markdown' require 'django.contrib.staticfiles' in INSTALLED_APPS

- Add 'django_markdown' to INSTALLED_APPS ::

    INSTALLED_APPS += ( 'django_markdown', )


- Add django_markdown urls to base urls ::

    url('^markdown/', include( 'django_markdown.urls')),


Use django_markdown
===================

#) Models: ::
    
    from django_markdown.models import MarkdownField
    class MyModel(models.Model):
        content = MarkdownField()

#) Custom forms: ::

    from django_markdown.fields import MarkdownFormField
    from django_markdown.widgets import MarkdownWidget
    class MyCustomForm(forms.Form):
        content = forms.CharField(widget=MarkdownWidget())
        content2 = MarkdownFormField()

#) Custom admins: ::

    from django_markdown.admin import MarkdownModelAdmin
    admin.site.register(MyModel, MarkdownModelAdmin)

#) Admin Overrides: (If you don't want to subclass package ModelAdmin's) ::

    from django.contrib import admin

    class YourModelAdmin(admin.ModelAdmin):
        formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}

#) Flatpages: ::

    # in your project main urls
    from django_markdown import flatpages
    ...
    # Django admin
    admin.autodiscover()
    flatpages.register()
    urlpatterns += [ url(r'^admin/', include(admin.site.urls)), ]

#) Template tags: ::

    <textarea name="test" id="new"></textarea>
    {% markdown_editor "#new" %}
    {% markdown_media %}


Settings
========

**MARKDOWN_EDITOR_SETTINGS** - holds the extra parameters set to be passed to ``textarea.markItUp()``

**MARKDOWN_EDITOR_SKIN** - skin option, default value is ``markitup``

Example: `settings.py` ::

    MARKDOWN_EDITOR_SKIN = 'simple'

**MARKDOWN_EXTENSIONS** - optional list of extensions passed to Markdown, discussed at https://pythonhosted.org/Markdown/extensions/index.html#officially-supported-extensions

Example: `settings.py` ::

    MARKDOWN_EXTENSIONS = ['extra']

**MARKDOWN_EXTENSION_CONFIGS** - Configure extensions, discussed at https://pythonhosted.org/Markdown/reference.html#extension_configs

**MARKDOWN_PREVIEW_TEMPLATE** - Template for preview a markdown. By default `django_markdown/preview.css`

**MARKDOWN_STYLE** - path to preview styles. By default `django_markdown/preview.css`

**MARKDOWN_SET_PATH** - path to folder with sets. By default `django_markdown/sets`

**MARKDOWN_SET_NAME** - name for current set. By default `markdown`.

**MARKDOWN_PROTECT_PREVIEW** - protect preview url for staff only


Examples
========

Execute `make run` in sources directory. Open http://127.0.0.1:8000 in your
browser. For admin access use 'root:root' credentials.


Changes
=======

Make sure you`ve read the following document if you are upgrading from previous versions:

http://packages.python.org/django-markdown/changes.html


Bug tracker
===========

If you have any suggestions, bug reports or
annoyances please report them to the issue tracker
at https://github.com/klen/django_markdown/issues


Contributing
============

Development of django-markdown happens at github: https://github.com/klen/django_markdown


Contributors
=============

* klen_ (Kirill Klenov)

* yavorskiy_ (Sergii Iavorskyi)


License
=======

Licensed under a `GNU lesser general public license`_.


Copyright
=========

Copyright (c) 2011 Kirill Klenov (horneds@gmail.com)

Markitup_:
    (c) 2008 Jay Salvat
    http://markitup.jaysalvat.com/ 
    

.. _GNU lesser general public license: http://www.gnu.org/copyleft/lesser.html
.. _pypi: http://packages.python.org/django-markdown/
.. _Markitup: http://markitup.jaysalvat.com/ 
.. _github: https://github.com/klen/django_markdown
.. _klen: https://github.com/klen
.. _yavorskiy: https://github.com/yavorskiy
