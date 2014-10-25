from django import forms
from .widgets import MarkdownWidget


class MarkdownFormField(forms.CharField):
    widget = MarkdownWidget
