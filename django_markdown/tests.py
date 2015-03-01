from django.test import TestCase
from django_markdown.utils import markdown as markdown_util

from django_markdown.templatetags.django_markdown import (
    markdown as markdown_tag
)


class DjangoMarkdownTagsTest(TestCase):

    def test_markdown_tag(self):
        html = markdown_tag('| header |\n| ---- |\n| data   |', 'tables')

        expected = ('<table>\n<thead>\n<tr>\n<th>header</th>'
                    '\n</tr>\n</thead>\n<tbody>\n<tr>\n<td>data'
                    '</td>\n</tr>\n</tbody>\n</table>')

        self.assertEqual(html, expected)


class DjangoMarkdownUtilsTest(TestCase):

    def test_markdown_util(self):
        html = markdown_util('**test**')
        expected = '<p><strong>test</strong></p>'

        self.assertEqual(html, expected)


class DjangoMarkdownViewsTest(TestCase):

    def test_preview_view(self):

        response = self.client.get('/markdown/preview/')
        self.assertContains(response, 'No content posted')
        self.assertContains(response, 'preview.css')

        response = self.client.get('/markdown/preview/', data=dict(
            data="# header \n *test*"))
        self.assertContains(response, '<h1>header</h1>')

        response = self.client.post('/markdown/preview/', data=dict(
            data="# header \n *test*"))
        self.assertContains(response, '<h1>header</h1>')

        from . import settings
        settings.MARKDOWN_PROTECT_PREVIEW = True
        response = self.client.get(
            '/markdown/preview/',
            data=dict(
                data="# header \n *test*"))
        self.assertEqual(response.status_code, 302)

        from django.contrib.auth import models
        user = models.User.objects.create(username='test', is_staff=True)
        user.set_password('test')
        user.save()
        self.client.login(username='test', password='test')

        response = self.client.get(
            '/markdown/preview/',
            data=dict(
                data="# header \n *test*"))
        self.assertContains(response, '<h1>header</h1>')
