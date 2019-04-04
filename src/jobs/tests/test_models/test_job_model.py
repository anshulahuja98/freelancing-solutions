from django.test import TestCase
from jobs.models import Skill, Job, Bid, RatingField
from accounts.models import Employer, Freelancer
from django.contrib.auth.models import User
from django_countries import countries
import tempfile
from django.db.models import Avg


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

        self.emp = Employer.objects.create(
            profile_image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            mobile=1234567890,
            description='emp_desc',
            country=countries[1][0],
            address='address',
            user=user,
        )

        self.job = Job.objects.create(
            employer=self.emp,
            title='title',
            description='job_desc',
            minimum_price=1,
            maximum_price=10
        )
        self.job.skills_required.add(self.skill1)
        self.job.skills_required.add(self.skill2)

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

        self.bid1 = Bid.objects.create(
            job=self.job,
            freelancer=self.freelancer,
            amount=1000,
            description='bid_desc1',
            additional_description='addn_desc1',
            comments='comment1',
            accepted=False,
            completed=False,
            rating=RatingField().get_choices()[2][0]
        )
        self.bid2 = Bid.objects.create(
            job=self.job,
            freelancer=self.freelancer,
            amount=12000,
            description='bid_desc2',
            additional_description='addn_desc2',
            comments='comment2',
            accepted=False,
            completed=False,
            rating=RatingField().get_choices()[3][0]
        )

    def test_skill_str_func(self):
        self.assertEquals(self.job.__str__(), self.job.title)

    def test_get_price_range(self):
        price_range = str(self.job.minimum_price) + '-' + str(self.job.maximum_price)
        self.assertEquals(self.job.get_price_range(), price_range)

    def test_job_skill_add(self):
        self.assertEquals(self.job.skills_required.all()[0], self.skill1)
        self.assertEquals(self.job.skills_required.all()[1], self.skill2)

    def test_get_average_bid(self):
        average_bid = Bid.objects.all().filter(job=self.job).aggregate(Avg('amount'))['amount__avg']
        self.assertEquals(self.job.get_average_bid, average_bid)
