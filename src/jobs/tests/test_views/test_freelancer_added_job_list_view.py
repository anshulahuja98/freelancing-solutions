from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import Freelancer
from django.contrib.auth.models import User


class TestFreelancerAddedJobListView(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:login')

        fr_test_user = User.objects.create_user(username='fr_testuser', password='1X<ISRUkw+tuK')
        fr_test_user.save()

        self.client.login(username='fr_testuser', password='1X<ISRUkw+tuK')

        self.fr = Freelancer.objects.create(
            user=fr_test_user
        )

    def test_freelancer_added_job_template_used(self):
        response = self.client.get(reverse('jobs:freelancer-job-list'))
        self.assertTemplateUsed(response, 'freelancer/job_list.html')
