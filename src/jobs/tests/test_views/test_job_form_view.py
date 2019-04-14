from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import Employer, Freelancer
from jobs.models import Skill
from jobs.forms import JobForm
from jobs.views import JobFormView
from django_countries import countries
import tempfile


class TestJobFormView(TestCase):
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

        self.user = User.objects.create(
            first_name='test_fn',
            last_name='test_ln',
            username='test_un'
        )

        self.emp = Employer.objects.create(
            profile_image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            mobile=1234567890,
            description='emp_desc',
            country=countries[1][0],
            address='address',
            user=self.user,
        )
        self.emp_pk = Employer.objects.get(pk=1).pk
        self.form_data = {
            'employer': self.emp_pk,
            'title': 'title',
            'description': 'job_desc',
            'minimum_price': 1,
            'maximum_price': 10,
            'skills_required': self.skills
        }

    def test_job_form_view_renders_employer_login(self):
        emp_test_user = User.objects.create_user(username='emp_testuser', password='1X<ISRUkw+tuK')
        emp_test_user.save()
        self.client.login(username='emp_testuser', password='1X<ISRUkw+tuK')
        self.emp = Employer.objects.create(
            user=emp_test_user
        )
        response = self.client.get(reverse('jobs:job-form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobs/form.html')

    def test_job_form_view_forbidden_freelancer_login(self):
        fr_test_user = User.objects.create_user(username='fr_testuser', password='1X<ISRUkw+tuK')
        fr_test_user.save()
        self.client.login(username='fr_testuser', password='1X<ISRUkw+tuK')
        self.emp = Freelancer.objects.create(
            user=fr_test_user
        )
        response = self.client.get(reverse('jobs:job-form'))
        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 403)
        self.assertTemplateNotUsed(response, 'jobs/form.html')

    def test_job_form_is_valid(self):
        form = JobForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_job_form_valid_function(self):
        form = JobForm(data=self.form_data)
        url = JobFormView.form_valid(JobFormView(), form).url + '/'
        self.assertEqual(reverse('jobs:employer-job-list'), url)

    def test_job_form_is_invalid(self):
        self.form_data = {
            'employer': self.emp_pk,
            'title': 'title',
            'description': 'job_desc',
            'minimum_price': 1,
            'skills_required': self.skills
        }
        form = JobForm(data=self.form_data)
        self.assertFalse(form.is_valid())
