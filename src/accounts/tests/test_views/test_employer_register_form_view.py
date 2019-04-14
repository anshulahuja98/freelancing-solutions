from django.test import TestCase, Client
from django.urls import reverse
from accounts.forms import EmployerRegisterForm
from accounts.views import EmployerRegisterFormView
from django_countries import countries


class TestEmployerRegisterFormView(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:login')

        self.form_data = {
            'first_name': 'test_fn',
            'last_name': 'test_ln',
            'username': 'test_un',
            'password1': 'sadkjGH#@#$$@23',
            'password2': 'sadkjGH#@#$$@23',
            'email': 'email@email.com',
            'description': 'job_desc',
            'mobile': 9348963248,
            'address': 'address',
            'country': countries[1][0],
        }

    def test_employer_register_form_is_valid(self):
        form = EmployerRegisterForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_employer_register_form_password_validation_fail(self):
        self.form_data = {
            'first_name': 'test_fn',
            'last_name': 'test_ln',
            'username': 'test_un',
            'password1': 'password',
            'password2': 'password',
            'email': 'email@email.com',
            'description': 'job_desc',
            'mobile': 9348963248,
            'address': 'address',
            'country': countries[1][0],
        }

        form = EmployerRegisterForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_employer_register_form_valid_function(self):
        form = EmployerRegisterForm(data=self.form_data)
        url = EmployerRegisterFormView.form_valid(EmployerRegisterFormView(), form).url
        self.assertEqual(reverse('accounts:login'), url)

    def test_employer_register_form_is_invalid(self):
        self.form_data = {
            'first_name': 'test_fn',
            'last_name': 'test_ln',
            'password2': 'password',
            'email': 'email@email.com',
            'description': 'job_desc',
            'mobile': 9348963248,
            'address': 'address',
            'country': countries[1][0],
        }
        form = EmployerRegisterForm(data=self.form_data)
        self.assertFalse(form.is_valid())
