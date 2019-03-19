from django.test import TestCase
from jobs.models import Skill, Job
from accounts.models import Employer
from django.contrib.auth.models import User
from django_countries import countries
import tempfile


class TestJobModel(TestCase):
    def setUp(self):
        self.skill1 = Skill.objects.create(
            name='skill1',
            abbr='skl1'
        )
        self.skill2 = Skill.objects.create(
            name='skill2',
            abbr='skl2'
        )

        user = User.objects.create(
            first_name='test_fn',
            last_name='test_ln',
            username='test_un'
        )

        emp = Employer.objects.create(
            profile_image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            mobile=1234567890,
            description='emp_desc',
            country=countries[1][0],
            address='address',
            user=user,
        )

        self.job = Job.objects.create(
            employer=emp,
            title='title',
            description='job_desc',
            minimum_price=1,
            maximum_price=10
        )
        self.job.skills_required.add(self.skill1)
        self.job.skills_required.add(self.skill2)

    def test_skill_str_func(self):
        self.assertEquals(self.job.__str__(), self.job.title)

    def test_get_price_range(self):
        price_range = str(self.job.minimum_price) + '-' + str(self.job.maximum_price)
        self.assertEquals(self.job.get_price_range(), price_range)

    def test_job_skill_add(self):
        self.assertEquals(self.job.skills_required.all()[0], self.skill1)
        self.assertEquals(self.job.skills_required.all()[1], self.skill2)
