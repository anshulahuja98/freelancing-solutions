from django.db import models
from accounts.models import Freelancer, Employer  # Import Freelancer and Employer modules from accounts
from .fields import MoneyField, RatingField  # Import custom Money and Rating fields from fields.py


# Module for handling skills of various freelancers
class Skill(models.Model):
    name = models.CharField(max_length=128)
    abbr = models.CharField(max_length=12, verbose_name="Abbreviation")

    # Returns string representation of Skill object - abbreviation of skill
    def __str__(self):
        return self.abbr


# Module for handling Jobs postings by the employers on the portal
class Job(models.Model):
    # Foreign key to an Employer object who has posted the job offering
    employer = models.ForeignKey(Employer, null=True, on_delete=models.SET_NULL)
    # Descriptive Fields for the Job
    title = models.CharField(max_length=128)
    description = models.TextField()
    # Many to Many relation to multiple skill objects required for the particular job, listed alongside jobs
    skills_required = models.ManyToManyField(Skill, default=None)
    # Price range for job set by employer
    minimum_price = MoneyField(null=True, blank=True)
    maximum_price = MoneyField()

    # Returns string representation of Job object - title of the Job
    def __str__(self):
        return self.title

    # Returns the average of all bids on particular Job
    @property
    def get_average_bid(self):
        return Bid.objects.all().filter(job=self).amount.average()

    # Returns price range as a string for the Job
    def get_price_range(self):
        return str(self.minimum_price) + '-' + str(self.maximum_price)


# Module for handling Bids by Freelancers on various Jobs
class Bid(models.Model):
    # Foreign key to a freelancer who bid on the job and employer who posted job
    job = models.ForeignKey(Job, null=True, on_delete=models.SET_NULL)
    freelancer = models.ForeignKey(Freelancer, null=True, on_delete=models.SET_NULL)
    # Amount of the bid made by freelancer
    amount = MoneyField()
    # Description Fields for the bid
    description = models.TextField()
    additional_description = models.TextField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    # Indicates acceptance of bid by employer
    accepted = models.BooleanField(default=False)
    # Indicates completion of Job by employer
    completed = models.BooleanField(default=False)
    # Rating provided by Employer to freelancer for job completion
    rating = RatingField()

    # Returns string representation of Bid object - title of the Job  along with name of freelancer's full name
    def __str__(self):
        return self.job.title + " (" + self.freelancer.user.get_full_name() + ")"
