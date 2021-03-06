from django.test import TestCase, Client
from django.urls import reverse


class TestGetViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:login')
        self.logout_url = reverse('accounts:logout')
        self.freelancer_register_url = reverse('accounts:freelancer-register')
        self.employer_register_url = reverse('accounts:employer-register')

    def test_login_GET(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_logout_GET(self):
        response = self.client.get(self.logout_url)

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse('main:index'), 302, 200)

    def test_freelancer_register_GET(self):
        response = self.client.get(self.freelancer_register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/freelancer-register.html')

    def test_employer_register_GET(self):
        response = self.client.get(self.employer_register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/employer-register.html')
