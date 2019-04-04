from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import Employer
from django.contrib.auth.models import User


class TestEmployerAddedJobListView(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:login')

        emp_test_user = User.objects.create_user(username='emp_testuser', password='1X<ISRUkw+tuK')
        emp_test_user.save()

        self.client.login(username='emp_testuser', password='1X<ISRUkw+tuK')

        self.emp = Employer.objects.create(
            user=emp_test_user
        )

    def test_employer_added_job_template_used(self):
        response = self.client.get(reverse('jobs:employer-job-list'))
        self.assertTemplateUsed(response, 'employer/job_list.html')
