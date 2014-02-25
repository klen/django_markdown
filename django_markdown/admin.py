""" Support Django admin. """

from django.contrib import admin
from django.db import models

from django_markdown.widgets import AdminMarkdownWidget


class MarkdownModelAdmin(admin.ModelAdmin):

    """ Support markdown as ModelAdmin. """

    formfield_overrides = {models.TextField: {'widget': AdminMarkdownWidget}}


class MarkdownInlineAdmin(admin.StackedInline):

    """ Support markdown as StackedInline. """

    formfield_overrides = {models.TextField: {'widget': AdminMarkdownWidget}}
