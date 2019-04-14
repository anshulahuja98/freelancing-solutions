from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .views import IndexView
from accounts.models import Freelancer, Employer


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:login')

        self.test_user = User.objects.create_user(username='testuser', password='1X<ISRUkw+tuK')
        self.client.login(username='testuser', password='1X<ISRUkw+tuK')

    def test_index_page_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('main:index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('main:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')

    def test_view_used(self):
        response = self.client.get(reverse('main:index'))
        self.assertEqual(response.resolver_match.func.__name__, IndexView.as_view().__name__)

    def test_freelancer_login_index_redirect(self):
        self.fr = Freelancer.objects.create(
            user=self.test_user
        )
        response = self.client.get(reverse('main:index'), follow=True)
        self.assertRedirects(response, reverse('freelancer:dashboard'))

    def test_employer_login_index_redirect(self):
        self.emp = Employer.objects.create(
            user=self.test_user
        )
        response = self.client.get(reverse('main:index'), follow=True)
        self.assertRedirects(response, reverse('employer:dashboard'))
