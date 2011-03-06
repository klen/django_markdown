..   -*- mode: rst -*-

django-markdown
###############

**Django markdown** is django application that allows use markdown wisywig in flatpages, admin forms and other forms.

.. contents::

Requirements
-------------

- python >= 2.5
- django >= 1.2
- markdown


Installation
------------

**Django markdown** should be installed using pip: ::

    pip install django-markdown


Setup
------

- Add 'django_markdown' to INSTALLED_APPS ::

    INSTALLED_APPS += ( 'django_markdown', )


- Add django_markdown urls to base urls ::

    url('^markdown/', include( 'django_markdown.urls')),


Use django_markdown
-------------------

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
--------

**MARKDOWN_SKIN** - skin option, default value is ``markitup``

Example: `settings.py` ::

    MARKDOWN_SKIN = 'simple'
