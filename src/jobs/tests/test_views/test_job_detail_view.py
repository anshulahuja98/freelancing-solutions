from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import Employer, Freelancer
from jobs.models import Skill, Job
from django_countries import countries
from jobs.views import JobDetailView
from django.http import Http404
from django.shortcuts import get_object_or_404
import tempfile
import uuid


class TestJobDetailView(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:login')
        self.skill1 = Skill.objects.create(
            name='skill1',
            abbr='skl1'
        )

        user = User.objects.create(
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
            user=user,
        )

        self.job = Job.objects.create(
            employer=self.emp,
            title='title',
            description='job_desc',
            minimum_price=1,
            maximum_price=10
        )
        self.job.skills_required.add(self.skill1)

    def test_job_detail_return_correct_job_object(self):
        job = Job.objects.filter(id=self.job.id)[0]
        view = JobDetailView()
        view.kwargs = dict(id=self.job.id)
        self.assertEquals(view.get_object(), job)

    def test_job_dont_exist(self):
        with self.assertRaises(Http404):
            get_object_or_404(Job, id=uuid.uuid4())

    def test_get_context_data_employer(self):
        emp_test_user = User.objects.create_user(username='emp_testuser', password='1X<ISRUkw+tuK')
        emp_test_user.save()
        self.client.login(username='emp_testuser', password='1X<ISRUkw+tuK')

        self.emp = Employer.objects.create(
            user=emp_test_user
        )
        response = self.client.get(reverse('jobs:job-detail', kwargs={'id': str(self.job.id)}))
        self.assertEqual(response.context_data['base_template'], 'employer/base.html')

    def test_get_context_data_freelancer(self):
        fr_test_user = User.objects.create_user(username='fr_testuser', password='1X<ISRUkw+tuK')
        fr_test_user.save()
        self.client.login(username='fr_testuser', password='1X<ISRUkw+tuK')

        self.fr = Freelancer.objects.create(
            user=fr_test_user
        )
        response = self.client.get(reverse('jobs:job-detail', kwargs={'id': str(self.job.id)}))
        self.assertEqual(response.context_data['base_template'], 'freelancer/base.html')
