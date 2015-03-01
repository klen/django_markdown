from django.test import TestCase
from django_markdown.utils import markdown as markdown_util

from django_markdown.templatetags.django_markdown import (
    markdown as markdown_tag
)

from django.contrib.auth import models


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

    def setUp(self):

        self.data = {'data': "# header \n *test*"}

    def test_preview_get_empty_request(self):

        response = self.client.get('/markdown/preview/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No content posted')
        self.assertContains(response, 'preview.css')

    def test_preview_get_markdown_request(self):

        response = self.client.get('/markdown/preview/', data=self.data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>header</h1>')

    def test_preview_post_markdown_request(self):

        data = {'data': "# header \n *test*"}

        response = self.client.post('/markdown/preview/', data=self.data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>header</h1>')

    def test_preview_MARKDOWN_PROTECT_PREVIEW(self):
        # monkey patching
        from . import settings
        settings.MARKDOWN_PROTECT_PREVIEW = True

        response = self.client.get('/markdown/preview/', data=self.data)

        self.assertEqual(response.status_code, 302)

        # for tests isolation reasons
        settings.MARKDOWN_PROTECT_PREVIEW = False

    def test_preview_get_markdown_for_admin_user_registered(self):

        username = 'test'
        password = 'test',

        user = models.User.objects.create(
            username=username,
            password=password,
            is_staff=True
        )

        self.client.login(username=username, password=password)

        response = self.client.get('/markdown/preview/', data=self.data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>header</h1>')
