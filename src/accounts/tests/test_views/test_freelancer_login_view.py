from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import Freelancer
from django.contrib.auth.models import User


class TestFreelancerLoginView(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:login')

        test_user = User.objects.create_user(username='testuser', password='1X<ISRUkw+tuK')
        test_user.save()

        self.fr = Freelancer.objects.create(
            user=test_user
        )

    def test_freelancer_correct_login(self):
        self.client.login(username='testuser', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('freelancer:dashboard'))

        self.assertEqual(str(response.context['user']), 'testuser')

    def test_freelancer_incorrect_login(self):
        self.client.login(username='testuser', password='1X<ISaUkw+tuK')
        response = self.client.get(reverse('freelancer:dashboard'))

        self.assertIsNone(response.context)

    def test_freelancer_login_redirects_to_correct_url(self):
        self.client.login(username='testuser', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('accounts:login'))

        self.assertRedirects(response, reverse('freelancer:dashboard'), 302, 200)

    def test_freelancer_login_redirects_to_employer_url(self):
        self.client.login(username='testuser', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('accounts:login'))
        redirect_url = response.url

        self.assertNotEquals(redirect_url, reverse('employer:dashboard'))
