from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django_countries.fields import CountryField


class AbstractUserProfile(models.Model):
    """Abstract User Profile model

    Fields:
        mobile_num_valid - Validate mobile numbers
        user - One to One field to user object of django's inbuilt auth User to handle authentication and basic details
        mobile - Mobile number of the user
        description - Details of the user
        address - Address of the user
        country - Country of the user
    """

    mobile_num_valid = RegexValidator(r'^\+?1?\d{9,15}$', message='Invalid mobile number.')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, validators=[mobile_num_valid])
    description = models.TextField()
    address = models.TextField()
    country = CountryField()

    class Meta:
        """Makes the class an Abstract class"""
        abstract = True


class Freelancer(AbstractUserProfile):
    """Module to handle Freelancer objects - inherits from AbstractUserProfile

    Fields:
        skills - M2M field to Skill object of the freelancer
        profile_image - Image of the user
    """
    skills = models.ManyToManyField('jobs.Skill', default=None)
    profile_image = models.ImageField(upload_to="freelancer-profile-images")

    def __str__(self):
        """Returns string representation of Freelancer object - full name of freelancer"""
        return self.user.get_full_name()


class Employer(AbstractUserProfile):
    """Module to handle Employer objects - inherits from AbstractUserProfile"""
    profile_image = models.ImageField(upload_to="employer-profile-images")

    def __str__(self):
        """Returns string representation of Employer object - full name of employer"""
        return self.user.get_full_name()
