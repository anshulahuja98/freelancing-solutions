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

    def __str__(self):
        return self.title

    @property
    def get_average_bid(self):
        return Bid.objects.all().filter(job=self).amount.average()

    def get_price_range(self):
        return self.minimum_price + '-' + self.maximum_price


class Bid(models.Model):
    RATINGS = (
        (0, 'NA'),
        (1, 'Very Poor'),
        (2, 'Poor'),
        (3, 'Average'),
        (4, 'Good'),
        (5, 'Excellent'),
    )
    # Foreign key to a freelancer and employer
    job = models.ForeignKey(Job, null=True, on_delete=models.SET_NULL)
    freelancer = models.ForeignKey(Freelancer, null=True, on_delete=models.SET_NULL)
    # Add tests for currency checks
    amount = MoneyField()
    description = models.TextField()
    additional_description = models.TextField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    accepted = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    rating = models.IntegerField(choices=RATINGS, default=0)

    def __str__(self):
        return self.job.title + " (" + self.freelancer.user.get_full_name() + ")"
