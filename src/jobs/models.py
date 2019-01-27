from django.db import models
from accounts.models import Freelancer, Employer


class Job(models.Model):
    employer = models.ForeignKey(Employer, null=True, on_delete=models.SET_NULL)

