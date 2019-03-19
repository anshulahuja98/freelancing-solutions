from django.test import TestCase
from jobs.models import Skill, Job, Bid, RatingField
from accounts.models import Employer, Freelancer
from django.contrib.auth.models import User
from django_countries import countries
import tempfile


class TestBidModel(TestCase):
    def setUp(self):
        self.skill1 = Skill.objects.create(
            name='skill1',
            abbr='skl1'
        )
        self.skill2 = Skill.objects.create(
            name='skill2',
            abbr='skl2'
        )

        emp_user = User.objects.create(
            first_name='test_fn_emp',
            last_name='test_ln_emp',
            username='test_un_emp'
        )
        emp = Employer.objects.create(
            profile_image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            mobile=1234567890,
            description='emp_desc',
            country=countries[1][0],
            address='emp_address',
            user=emp_user,
        )

        fr_user = User.objects.create(
            first_name='test_fn_fr',
            last_name='test_ln_fr',
            username='test_un_fr'
        )
        self.freelancer = Freelancer.objects.create(
            profile_image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            mobile=1234567890,
            description='fr_desc',
            country=countries[0][0],
            address='fr_address',
            user=fr_user,
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

        self.bid = Bid.objects.create(
            job=self.job,
            freelancer=self.freelancer,
            amount=1000,
            description='bid_desc',
            additional_description='addn_desc',
            comments='comment',
            accepted=False,
            completed=False,
            rating=RatingField().get_choices()[2][0]
        )

    def test_bid_str_func(self):
        self.assertEquals(self.bid.__str__(), self.job.title + " (" + self.freelancer.user.get_full_name() + ")")
