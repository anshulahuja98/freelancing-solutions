from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import Freelancer


class TestBidListView(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:login')

        self.test_user = User.objects.create_user(username='testuser', password='1X<ISRUkw+tuK')
        self.test_user.save()
        self.client.login(username='testuser', password='1X<ISRUkw+tuK')

    def test_correct_bid_list_view_render_freelancer_login(self):
        self.fr = Freelancer.objects.create(
            user=self.test_user
        )
        response = self.client.get(reverse('freelancer:bid-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'freelancer/bid_list.html')

    # def test_correct_bid_list_view_render_employer_login(self):
    #     self.emp = Employer.objects.create(
    #         user=self.test_user
    #     )
    #     print(self.client.get(reverse('employer:bid-list')))
    #     response = self.client.get(reverse('employer:bid-list'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'freelancer/bid_list.html')
