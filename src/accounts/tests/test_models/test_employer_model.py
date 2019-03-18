from django.test import TestCase
from accounts.models import Employer
from django.contrib.auth.models import User
from django_countries import countries
import tempfile


class TestEmployerModel(TestCase):

    def setUp(self):
        self.user2 = User.objects.create(
            first_name='test_fn_2',
            last_name='test_ln_2',
            username='test_un_2'
        )

        self.employer1 = Employer.objects.create(
            profile_image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            mobile=1234567890,
            description='user_desc2',
            country=countries[1][0],
            address='address2',
            user=self.user2,
        )

    def test_employer_create(self):
        self.assertEquals(self.employer1.description, 'user_desc2')
        self.assertEquals(self.employer1.country, countries[1][0])
        self.assertEquals(self.employer1.address, 'address2')
        self.assertEquals(self.employer1.mobile, 1234567890)

    def test_employer_user_add(self):
        self.assertEquals(self.employer1.user.first_name, self.user2.first_name)
        self.assertEquals(self.employer1.user.last_name, self.user2.last_name)
        self.assertEquals(self.employer1.user.username, self.user2.username)

    def test_employer_str_func(self):
        self.assertEquals(self.employer1.__str__(), self.user2.get_full_name())

    def test_mobile_max_length(self):
        max_length = self.employer1._meta.get_field('mobile').max_length
        self.assertEquals(max_length, 15)
