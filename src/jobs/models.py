from django.db import models
from accounts.models import Freelancer, Employer
from .fields import MoneyField


class Skill(models.Model):
    name = models.CharField(max_length=128)
    abbr = models.CharField(max_length=12)

    def __str__(self):
        return self.abbr


class Job(models.Model):
    employer = models.ForeignKey(Employer, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=128)
    description = models.TextField()
    skills_required = models.ManyToManyField(Skill, default=None)
    # Price range
    minimum_price = MoneyField(null=True, blank=True)
    maximum_price = MoneyField()


class Bid(models.Model):
    # Foreign key to a freelancer and employer
    job = models.ForeignKey(Job, null=True, on_delete=models.SET_NULL)
    freelancer = models.ForeignKey(Freelancer, null=True, on_delete=models.SET_NULL)
    # Add tests for currency checks
    amount = MoneyField()
    description = models.TextField()
    additional_description = models.TextField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.job.title + " (" + self.freelancer.user.get_full_name() + ")"
