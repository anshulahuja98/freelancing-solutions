from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import FreelancerRegisterFormView, EmployerRegisterFormView, LoginView
from django.contrib.auth.views import LogoutView


class TestURLsResolves(SimpleTestCase):

    def test_login_url_resolves(self):
        url = reverse('accounts:login')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_logout_url_resolves(self):
        url = reverse('accounts:logout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_freelancer_register_url_resolves(self):
        url = reverse('accounts:freelancer-register')
        self.assertEquals(resolve(url).func.view_class, FreelancerRegisterFormView)

    def test_employer_register_url_resolves(self):
        url = reverse('accounts:employer-register')
        self.assertEquals(resolve(url).func.view_class, EmployerRegisterFormView)
