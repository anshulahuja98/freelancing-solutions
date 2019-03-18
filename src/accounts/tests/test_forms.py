from django.test import TestCase

from accounts.forms import FreelancerRegisterForm, EmployerRegisterForm, CountryField
from django.contrib.auth import password_validation


class TestRegistrationForm(TestCase):

    def setUp(self):
        self.form = FreelancerRegisterForm(data={
            'mobile': 1234567890,
            'description': 'user_desc1',
            'country': CountryField().countries[0][0],
            'address': 'address1',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'username': 'username',
            'email': 'gg@gmail.com',
            'password1': 'Password123!',
            'password2': 'Password123!'
        })

    def test_password1_field_label(self):
        self.assertTrue(
            self.form.fields['password1'].label is None or self.form.fields['password1'].label == 'Password')

    def test_password1_field_help_text(self):
        self.assertEqual(self.form.fields['password1'].help_text,
                         password_validation.password_validators_help_text_html())

    def test_password2_field_label(self):
        self.assertTrue(self.form.fields['password2'].label == 'Password confirmation')

    def test_mobile_max_length(self):
        max_length = self.form.fields['mobile'].max_length
        self.assertEquals(max_length, 15)

    def test_form_valid_data(self):
        self.assertTrue(self.form.is_valid())

    def test_form_invalid_mobile_max_length(self):
        self.form.data['mobile'] = 12345678901234567890
        self.assertFalse(self.form.is_valid())

    def test_form_password_mismatch(self):
        self.form.data['password2'] = 'passmismatch'
        self.assertFalse(self.form.is_valid())

    def test_form_invalid_email(self):
        self.form.data['email'] = 'wrong_email'
        self.assertFalse(self.form.is_valid())

    def test_form_invalid_country(self):
        self.form.data['country'] = 'wrong_country'
        self.assertFalse(self.form.is_valid())

    def test_form_unfilled_data(self):
        form = FreelancerRegisterForm(data={
            'mobile': 1234567890,
            'country': CountryField().countries[0][0],
            'address': 'address1',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'gg@gmail.com',
            'password1': 'Password123!',
            'password2': 'Password123!'
        })
        self.assertFalse(form.is_valid())

    def test_employer_form_valid_data(self):
        form = EmployerRegisterForm(data={
            'mobile': 1234567890,
            'description': 'user_desc1',
            'country': CountryField().countries[0][0],
            'address': 'address1',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'username': 'username',
            'email': 'gg@gmail.com',
            'password1': 'Password123!',
            'password2': 'Password123!'
        })
        self.assertTrue(form.is_valid())
