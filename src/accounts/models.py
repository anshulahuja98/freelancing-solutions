from django.db import models
from django.contrib.auth.models import User


# Userprofile models for different type of users

class Freelancer(models.Model):
    # Foreign key to django's inbuilt user model which handles authentication and basic details related to a user like name, email etc
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Employer(models.Model):
    # Foreign key to django's inbuilt user model which handles authentication and basic details related to a user like name, email etc
    user = models.OneToOneField(User, on_delete=models.CASCADE)
