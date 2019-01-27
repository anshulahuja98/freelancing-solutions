from django.db import models
from accounts.models import Freelancer, Employer


class Job(models.Model):
    employer = models.ForeignKey(Employer, null=True, on_delete=models.SET_NULL)


class Bid(models.Model):
    # Foreign key to a freelancer and employer
    job = models.ForeignKey(Job, null=True, on_delete=models.SET_NULL)
    freelancer = models.ForeignKey(Freelancer, null=True, on_delete=models.SET_NULL)
    # Add tests for currency checks
    bid_amount = models.DecimalField(max_digits=8, decimal_places=2)
