from django import forms
from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from django_markdown.widgets import MarkdownWidget


class LocalFlatPageForm(FlatpageForm):
    content = forms.CharField(widget=MarkdownWidget)


class LocalFlatPageAdmin(FlatPageAdmin):
    form = LocalFlatPageForm


def register():
    admin.site.unregister(FlatPage)
    admin.site.register(FlatPage, LocalFlatPageAdmin)
