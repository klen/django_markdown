""" Support Django admin. """

from django.contrib.admin import (
    ModelAdmin, StackedInline
)

from .widgets import AdminMarkdownWidget
from .models import MarkdownField


class MarkdownModelAdmin(ModelAdmin):

    """ Support markdown as ModelAdmin. """

    formfield_overrides = {
        MarkdownField: {
            'widget': AdminMarkdownWidget
        }
    }


class MarkdownInlineAdmin(StackedInline):

    """ Support markdown as StackedInline. """

    formfield_overrides = {
        MarkdownField: {
            'widget': AdminMarkdownWidget
        }
    }
