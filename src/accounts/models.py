from django.db import models
from django.contrib.auth.models import \
    User  # Refers to django's inbuilt auth User for handling authentication and basic details
from django.core.validators import RegexValidator  # Regex validator module
from django_countries.fields import CountryField


# Abstract User Profile model
class AbstractUserProfile(models.Model):
    # Regex Validators
    # Regex validator for checking phone numbers
    mobile_num_valid = RegexValidator(r'^\+?1?\d{9,15}$', message='Invalid mobile number.')
    # Fields
    # One to One field to user object of django's inbuilt auth User to handle authentication and basic details
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional userprofile details
    mobile = models.CharField(max_length=15, validators=[mobile_num_valid])
    description = models.TextField()
    address = models.TextField()
    country = CountryField()

    class Meta:
        # Makes the class an Abstract class
        abstract = True


# Module to handle Freelancer objects - inherits from AbstractUserProfile
class Freelancer(AbstractUserProfile):
    # Many to many field to skills of the freelancer
    skills = models.ManyToManyField('jobs.Skill', default=None)
    profile_image = models.ImageField(upload_to="freelancer-profile-images")

    # Returns string representation of Freelancer object - full name of freelancer
    def __str__(self):
        return self.user.get_full_name()


# Module to handle Employer objects - inherits from AbstractUserProfile
class Employer(AbstractUserProfile):
    profile_image = models.ImageField(upload_to="employer-profile-images")

    # Returns string representation of Employer object - full name of employer
    def __str__(self):
        return self.user.get_full_name()
