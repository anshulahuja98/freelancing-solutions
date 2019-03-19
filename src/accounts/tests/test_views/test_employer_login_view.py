from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import Employer
from django.contrib.auth.models import User


class TestEmployerLoginView(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:login')

        test_user = User.objects.create_user(username='testuser', password='1X<ISRUkw+tuK')
        test_user.save()

        self.fr = Employer.objects.create(
            user=test_user
        )

    def test_employer_correct_login(self):
        self.client.login(username='testuser', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('employer:dashboard'))

        self.assertEqual(str(response.context['user']), 'testuser')

    def test_employer_incorrect_login(self):
        self.client.login(username='testuser', password='1X<ISaUkw+tuK')
        response = self.client.get(reverse('employer:dashboard'))

        self.assertIsNone(response.context)

    def test_employer_login_redirects_to_correct_url(self):
        self.client.login(username='testuser', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('accounts:login'))

        self.assertRedirects(response, reverse('employer:dashboard'), 302, 200)

    def test_employer_login_redirects_to_employer_url(self):
        self.client.login(username='testuser', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('accounts:login'))
        redirect_url = response.url

        self.assertNotEquals(redirect_url, reverse('freelancer:dashboard'))
