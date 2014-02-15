django-markdown
###############

.. _description:

**Django markdown** is django application that allows use markdown wysiwyg in flatpages, admin forms and other forms.
Documentaton available at pypi_ or github_.

.. _badges:

.. image:: https://secure.travis-ci.org/klen/django_markdown.png?branch=develop
    :target: http://travis-ci.org/klen/django_markdown
    :alt: Build Status

.. image:: https://coveralls.io/repos/klen/django_markdown/badge.png?branch=develop
    :target: https://coveralls.io/r/klen/django_markdown?branch=develop
    :alt: Coveralls

.. image:: https://pypip.in/v/django-markdown/badge.png
    :target: https://crate.io/packages/django_markdown
    :alt: Version

.. image:: https://pypip.in/d/django-markdown/badge.png
    :target: https://crate.io/packages/django_markdown
    :alt: Downloads

.. image:: https://dl.dropboxusercontent.com/u/487440/reformal/donate.png
    :target: https://www.gittip.com/klen/
    :alt: Donate


.. contents::

.. _requirements:

Requirements
============

- python >= 2.6
- django >= 1.4
- markdown


.. _installation:

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

#) Custom forms: ::

    from django_markdown.widgets import MarkdownWidget
    class MyCustomForm(forms.Form):
        content = forms.CharField( widget=MarkdownWidget() )

#) Custom admins: ::

    from django_markdown.admin import MarkdownModelAdmin
    admin.site.register(MyModel, MarkdownModelAdmin)

#) Flatpages: ::

    # in your project main urls
    from django_markdown import flatpages
    ...
    # Django admin
    admin.autodiscover()
    flatpages.register()
    urlpatterns += [ url(r'^admin/', include(admin.site.urls)), ]

#) JavaScript API: ::

    // Editors manager ``miu`` methods

    // Initialize editor using default settings extended with ``extraSettings``
    miu.init(textareaId, extraSettings);

    // Get default mIu settings
    miu.settings();

    // Set default mIu settings
    miu.settings(newSettings);
    
    // Get all initialized aditors
    miu.editors();
    
    // Get certain editor
    miu.editors(textareaId);
    
    
    // Editor instance methods
    
    // Dynamically add button at ``index`` position 
    editor.addButton(conf, index)
    
    // Dynamically remove button at ``index`` position
    editor.removeButton(index)
    

Settings
========

**MARKDOWN_EDITOR_SKIN** - skin option, default value is ``markitup``

Example: `settings.py` ::

    MARKDOWN_EDITOR_SKIN = 'simple'

**MARKDOWN_EDITOR_SETTINGS** - holds the extra parameters set to be passed to textarea.markItUp() 


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
