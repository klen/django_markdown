from django.db import models
from .fields import MarkdownFormField


class MarkdownField(models.TextField):
    def formfield(self, **kwargs):
        defaults = {'form_class': MarkdownFormField}
        defaults.update(kwargs)
        return super(MarkdownField, self).formfield(**defaults)
