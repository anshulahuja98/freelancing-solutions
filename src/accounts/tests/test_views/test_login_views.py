from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestLoginView(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:login')

        test_user = User.objects.create_user(username='testuser', password='3HJ1aV0sZ&3iD')
        test_user.save()

    def test_valid_login(self):
        self.client.login(username='testuser', password='3HJ1aV0sZ&3iD')
        response = self.client.get(reverse('main:index'))

        self.assertEquals(str(response.context['user']), 'testuser')

    def test_invalid_login(self):
        self.client.login(username='testuser', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('main:index'))

        self.assertNotEquals(str(response.context['user']), 'testuser')
        self.assertEquals(str(response.context['user']), 'AnonymousUser')
