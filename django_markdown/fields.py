from django import forms
from .widgets import MarkdownWidget


class MarkdownFormField(forms.CharField):
    def __init__(self, *args, **kwargs):
        # Django admin overrides the 'widget' value so this seems the only way
        # to scupper it!
        super().__init__(*args, **kwargs)
        self.widget = MarkdownWidget()
