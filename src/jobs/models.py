from django.db import models
from accounts.models import Freelancer, Employer  # Import Freelancer and Employer modules from accounts
from .fields import MoneyField, RatingField  # Import custom Money and Rating fields from fields.py
from django.db.models import Avg
from uuid import uuid4
from django.shortcuts import reverse


class Skill(models.Model):
    """Module for handling skills of various freelancers."""

    name = models.CharField(max_length=128)
    abbr = models.CharField(max_length=12, verbose_name="Abbreviation")

    def __str__(self):
        """Returns string representation of Skill object - abbreviation of skill."""
        return self.abbr


class Job(models.Model):
    """Module for handling Jobs postings by the employers on the portal

    Description of fields used for the model:
        id - Unique ID for each Job
        employer - Foreign key to an Employer object who has posted the job offering
        title - Job name
        description - Job Details
        skills_required - M2M relation to Skill object required for the particular job, listed alongside jobs
        minimum_price/maximum_price - Price range for job set by employer
    """

    id = models.UUIDField(primary_key=True, default=uuid4)
    employer = models.ForeignKey(Employer, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=128)
    description = models.TextField()
    skills_required = models.ManyToManyField(Skill, default=None)
    minimum_price = MoneyField(null=True, blank=True)
    maximum_price = MoneyField()

    def __str__(self):
        """ Returns string representation of Job object - title of the Job """
        return self.title

    @property
    def get_average_bid(self):
        """Returns the average of all bids on particular Job"""
        return Bid.objects.all().filter(job=self).aggregate(Avg('amount'))['amount__avg']

    def get_price_range(self):
        """Returns price range as a string for the Job"""
        return str(self.minimum_price) + '-' + str(self.maximum_price)

    def get_absolute_url(self):
        """Returns current job detail url"""
        return reverse("jobs:job-detail", kwargs={"id": self.id})

    def get_jobs_without_accepted_bids(self):
        accepted_bids = Bid.objects.all().filter(accepted=True).values_list('job').distinct()
        job = Job.objects.all().difference(Job.objects.all().filter(id__in=accepted_bids))
        return job

    def get_jobs_by_skills(self, freelancer_user_profile):
        jobs_without_bids = Job.get_jobs_without_accepted_bids(self)
        return jobs_without_bids.filter(skills_required__in=freelancer_user_profile.skills.all()).distinct()


class Bid(models.Model):
    """Module for handling Bids by Freelancers on various Jobs

    Description of fields used for the model:
        job - Foreign key to a freelancer who bid on the job and employer who posted job
        amount - Amount of the bid made by freelancer
        description/additional_description - Description of what Freelancer will do for the job
        comments - Comments for what extra info needed by Freelancer for the job
        accepted - Indicates acceptance of bid by employer
        completed - Indicates completion of Job by employer
        rating - Rating provided by Employer to freelancer for job completion
    """
    #
    job = models.ForeignKey(Job, null=True, on_delete=models.SET_NULL)
    freelancer = models.ForeignKey(Freelancer, null=True, on_delete=models.SET_NULL)
    amount = MoneyField()
    description = models.TextField()
    additional_description = models.TextField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    accepted = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    rating = RatingField()

    def __str__(self):
        """Returns string representation of Bid object - title of the Job along with name of freelancer's full name"""
        return self.job.title + " (" + self.freelancer.user.get_full_name() + ")"
