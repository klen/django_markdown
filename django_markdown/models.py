from django.db import models
from .widgets import MarkdownWidget


class MarkdownField(models.TextField):
    def formfield(self, **kwargs):
        defaults = {'widget': MarkdownWidget}
        defaults.update(kwargs)
        return super(MarkdownField, self).formfield(**defaults)
