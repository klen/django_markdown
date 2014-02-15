from django import forms
from django_markdown.widgets import MarkdownWidget


class CustomForm(forms.Form):

    content = forms.CharField(widget=MarkdownWidget())
