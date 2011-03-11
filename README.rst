django-markdown
###############

**Django markdown** is django application that allows use markdown wysiwyg in flatpages, admin forms and other forms.
Documentaton available at pypi_ or github_.

.. contents::

Requirements
============

- python >= 2.5
- django >= 1.2
- markdown


Installation
============

**Django markdown** should be installed using pip: ::

    pip install django-markdown


Setup
=====

- Add 'django_markdown' to INSTALLED_APPS ::

    INSTALLED_APPS += ( 'django_markdown', )


- Add django_markdown urls to base urls ::

    url('^markdown/', include( 'django_markdown.urls')),


Use django_markdown
===================

1) Custom forms: ::

    from django_markdown.widgets import MarkdownWidget
    class MyCustomForm(forms.Form):
        content = forms.CharField( widget=MarkdownWidget() )

2) Custom admins: ::

    from django_markdown.admin import MarkdownModelAdmin
    adimin.site.register(MyModel, MarkdownModelAdmin)

3) Flatpages: ::

    # in your project main urls
    from django_markdown import flatpages
    ...
    # Django admin
    admin.autodiscover()
    flatpages.register()
    urlpatterns += [ url(r'^admin/', include(admin.site.urls)), ]


Settings
========

**MARKDOWN_SKIN** - skin option, default value is ``markitup``

Example: `settings.py` ::

    MARKDOWN_SKIN = 'simple'

**MARKDOWN_EDITOR_SETTINGS** - holds the extra parameters set to be passed to textarea.markItUp() 


Changes
=======

Make sure you`ve read the following document if you are upgrading from previous versions of scss:

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
.. _github: https://github.com/klen/python-scss
.. _klen: https://github.com/klen
.. _yavorskiy: https://github.com/yavorskiy
