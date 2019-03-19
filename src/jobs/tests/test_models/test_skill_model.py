from django.test import TestCase
from jobs.models import Skill


class TestSkillModel(TestCase):
    def setUp(self):
        self.skill = Skill.objects.create(
            name='skill',
            abbr='skl'
        )

    def test_skill_create(self):
        self.assertEquals(self.skill.name, 'skill')
        self.assertEquals(self.skill.abbr, 'skl')

    def test_skill_str_func(self):
        self.assertEquals(self.skill.__str__(), self.skill.abbr)
