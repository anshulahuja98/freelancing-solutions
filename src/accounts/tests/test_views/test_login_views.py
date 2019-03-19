from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestLoginView(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:login')

        self.test_user = User.objects.create_user(username='testuser', password='3HJ1aV0sZ&3iD')
        self.test_user.save()

        self.test_admin = User.objects.create_superuser(username='admin_user', email='admin@test.com',
                                                        password='AHJ1aV0sZ&3iD')
        self.test_admin.save()

    def test_valid_login(self):
        self.client.login(username='testuser', password='3HJ1aV0sZ&3iD')
        response = self.client.get(reverse('main:index'))

        self.assertEquals(str(response.context['user']), 'testuser')

    def test_invalid_login(self):
        self.client.login(username='testuser', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('main:index'))

        self.assertNotEquals(str(response.context['user']), 'testuser')
        self.assertEquals(str(response.context['user']), 'AnonymousUser')

    def test_valid_admin_login(self):
        self.client.login(username='admin_user', password='AHJ1aV0sZ&3iD')
        response = self.client.get(reverse('main:index'))

        self.assertEquals(str(response.context['user']), 'admin_user')

    def test_admin_valid_redirect(self):
        self.client.login(username='admin_user', password='AHJ1aV0sZ&3iD')
        response = self.client.get(reverse('accounts:login'))

        self.assertRedirects(response, '/admin', 302, 301)

    def test_admin_portal_access(self):
        self.client.login(username='admin_user', password='AHJ1aV0sZ&3iD')
        response = self.client.get('/admin/')

        self.assertIsNotNone(response)
        self.assertEquals(response.status_code, 200)

    def test_admin_is_staff(self):
        self.assertTrue(self.test_admin.is_staff)

    def test_user_is_not_staff(self):
        self.assertFalse(self.test_user.is_staff)

    def test_user_portal_no_access(self):
        self.client.login(username='testuser', password='3HJ1aV0sZ&3iD')
        response = self.client.get('/admin/')

        self.assertRedirects(response, '/admin/login/?next=/admin/', 302, 200)
