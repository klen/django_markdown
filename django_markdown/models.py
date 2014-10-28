from django.db import models
from .fields import MarkdownFormField
from .widgets import MarkdownWidget


class MarkdownField(models.TextField):
    def formfield(self, **kwargs):
        defaults = {'form_class': MarkdownFormField}
        defaults.update(kwargs)
        return super(MarkdownField, self).formfield(**defaults)
