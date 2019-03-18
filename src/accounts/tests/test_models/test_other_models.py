from django.test import TestCase
from jobs.models import Skill
from django.contrib.auth.models import User


class TestSkillModel(TestCase):
    def setUp(self):
        self.skill1 = Skill.objects.create(
            name='skill1',
            abbr='skill1'
        )

    def test_skill_create(self):
        self.assertEquals(self.skill1.name, 'skill1')


class TestUserModel(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            first_name='test1',
            last_name='test1',
            username='test1'
        )

    def test_user_create(self):
        self.assertEquals(self.user1.username, 'test1')
        self.assertEquals(self.user1.first_name, 'test1')
        self.assertEquals(self.user1.last_name, 'test1')

