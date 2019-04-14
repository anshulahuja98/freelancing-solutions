from django.test import TestCase, Client
from django.urls import reverse
from jobs.models import Skill
from accounts.forms import FreelancerRegisterForm
from accounts.views import FreelancerRegisterFormView
from django_countries import countries


class TestFreelancerRegisterFormView(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:login')
        self.skill1 = Skill.objects.create(
            name='skill1',
            abbr='skl1'
        )
        self.skill2 = Skill.objects.create(
            name='skill2',
            abbr='skl2'
        )
        self.skills = [self.skill1, self.skill2]

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
            'skills': self.skills
        }

    def test_freelancer_register_form_is_valid(self):
        form = FreelancerRegisterForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_freelancer_register_form_password_validation_fail(self):
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
            'skills': self.skills
        }

        form = FreelancerRegisterForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_freelancer_register_form_valid_function(self):
        form = FreelancerRegisterForm(data=self.form_data)
        url = FreelancerRegisterFormView.form_valid(FreelancerRegisterFormView(), form).url
        self.assertEqual(reverse('accounts:login'), url)

    def test_freelancer_register_form_is_invalid(self):
        self.form_data = {
            'first_name': 'test_fn',
            'last_name': 'test_ln',
            'password2': 'password',
            'email': 'email@email.com',
            'description': 'job_desc',
            'mobile': 9348963248,
            'address': 'address',
            'country': countries[1][0],
            'skills': self.skills
        }
        form = FreelancerRegisterForm(data=self.form_data)
        self.assertFalse(form.is_valid())
