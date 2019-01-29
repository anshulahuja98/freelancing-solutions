from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Abstract User Profile model
class AbstractUserProfile(models.Model):
    # Regex Validators
    mobile_num_valid = RegexValidator(r'^[0-9]{10}$', message='Not a valid mobile number!')

    # Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10, validators=[mobile_num_valid])
    description = models.TextField()

    class Meta:
        abstract = True


class Freelancer(AbstractUserProfile):
    # Foreign key to django's inbuilt user model which handles authentication and basic details related to a user
    skills = models.ManyToManyField('jobs.Skill', default=None)
    profile_image = models.ImageField(upload_to="freelancer-profile-images")

    def __str__(self):
        return self.user.get_full_name()


class Employer(AbstractUserProfile):
    # Foreign key to django's inbuilt user model which handles authentication and basic details related to a user
    profile_image = models.ImageField(upload_to="employer-profile-images")

    def __str__(self):
        return self.user.get_full_name()
