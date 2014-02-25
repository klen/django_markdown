""" Support markdown by Django Flatpages admin. """

from django import forms
from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from django_markdown.widgets import AdminMarkdownWidget


class LocalFlatPageForm(FlatpageForm):

    """ Markdown support. """

    content = forms.CharField(widget=AdminMarkdownWidget)


class LocalFlatPageAdmin(FlatPageAdmin):

    """ Markdown support. """

    form = LocalFlatPageForm


def register():
    """ Register markdown for flatpages. """

    admin.site.unregister(FlatPage)
    admin.site.register(FlatPage, LocalFlatPageAdmin)
