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
        self.user2 = User.objects.create(
            first_name='test2',
            last_name='test2',
            username='test2'
        )

        self.skill1 = Skill.objects.create(
            name='skill1',
            abbr='skill1'
        )
        self.skill2 = Skill.objects.create(
            name='skill2',
            abbr='skill2'
        )

        self.freelancer1 = Freelancer.objects.create(
            profile_image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            mobile=1234567890,
            description='user_desc1',
            country='country1',
            address='address1',
            user=self.user1,
        )
        self.freelancer1.skills.add(self.skill1)
        self.freelancer1.skills.add(self.skill2)

        self.employer1 = Employer.objects.create(
            profile_image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            mobile=1234567890,
            description='user_desc2',
            country='country2',
            address='address2',
            user=self.user2,
        )

    def test_user_create(self):
        self.assertEquals(self.user1.first_name, 'test1')
        self.assertEquals(self.user1.last_name, 'test1')
        self.assertEquals(self.user1.username, 'test1')

    def test_skill_create(self):
        self.assertEquals(self.freelancer1.skills.first().name, 'skill1')

    def test_freelancer_create(self):
        self.assertEquals(self.freelancer1.description, 'user_desc1')
        self.assertEquals(self.freelancer1.country, 'country1')
        self.assertEquals(self.freelancer1.address, 'address1')
        self.assertEquals(self.freelancer1.mobile, 1234567890)

    def test_freelancer_user_add(self):
        self.assertEquals(self.freelancer1.user.first_name, self.user1.first_name)
        self.assertEquals(self.freelancer1.user.last_name, self.user1.last_name)
        self.assertEquals(self.freelancer1.user.username, self.user1.username)

    def test_freelancer_skills_add(self):
        self.assertEquals(self.freelancer1.skills.all()[0].name, 'skill1')
        self.assertEquals(self.freelancer1.skills.all()[1].name, 'skill2')

    def test_employer_create(self):
        self.assertEquals(self.employer1.description, 'user_desc2')
        self.assertEquals(self.employer1.country, 'country2')
        self.assertEquals(self.employer1.address, 'address2')
        self.assertEquals(self.employer1.mobile, 1234567890)

    def test_employer_user_add(self):
        self.assertEquals(self.employer1.user.first_name, self.user2.first_name)
        self.assertEquals(self.employer1.user.last_name, self.user2.last_name)
        self.assertEquals(self.employer1.user.username, self.user2.username)
