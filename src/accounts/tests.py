from django.test import TestCase


class LoginViewTest(TestCase):

    def test_login_redirect(self):
        response = self.client.post('/accounts/login')
        self.assertRedirects(response, '/accounts/login/', status_code=301, target_status_code=200)

    def test_login(self):
        response = self.client.post('/accounts/login/')
        self.assertTemplateUsed(response, 'accounts/login.html')


