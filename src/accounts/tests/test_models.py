from django.test import TestCase
from accounts.models import Freelancer, Employer, AbstractUserProfile, CountryField
from jobs.models import Skill
from django.contrib.auth.models import User
import tempfile


class TestModels(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(
            first_name='test1',
            last_name='test1',
            username='test1'
        )
        self.skill1 = Skill.objects.create(
            name='skill1',
            abbr='skill1'
        )
        self.freelancer1 = Freelancer.objects.create(
            profile_image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            mobile=9432423223,
            description='user_desc1',
            country='country1',
            address='address1',
            user=self.user1,
        )
        self.freelancer1.skills.add(self.skill1)
