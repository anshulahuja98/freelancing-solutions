from django.test import TestCase
from django.urls import reverse
from .views import IndexView


class IndexViewTest(TestCase):

    def test_index_page_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')

    def test_view_used(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.resolver_match.func.__name__, IndexView.as_view().__name__)
