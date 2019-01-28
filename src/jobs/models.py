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


class Bid(models.Model):
    # Foreign key to a freelancer and employer
    job = models.ForeignKey(Job, null=True, on_delete=models.SET_NULL)
    freelancer = models.ForeignKey(Freelancer, null=True, on_delete=models.SET_NULL)
    # Add tests for currency checks
    bid_amount = models.DecimalField(max_digits=8, decimal_places=2)
