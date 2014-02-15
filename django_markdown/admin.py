from django.contrib import admin
from django.db import models

from django_markdown.widgets import MarkdownWidget


class MarkdownModelAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': MarkdownWidget}}

class MarkdownInlineAdmin(admin.StackedInline):
    formfield_overrides = {models.TextField: {'widget': MarkdownWidget}}
