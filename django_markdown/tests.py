from django.test import TestCase


class DjangoMarkdownTestCase(TestCase):

    def test_base(self):
        self.assertTrue(True)

    def test_preview_view(self):
        response = self.client.get('/markdown/preview/')
        self.assertContains(response, 'No content posted')
        self.assertContains(response, 'preview.css')

        response = self.client.get('/markdown/preview/', data=dict(
            data="# header \n *test*"
        ))
        self.assertContains(response, '<h1>header</h1>')
