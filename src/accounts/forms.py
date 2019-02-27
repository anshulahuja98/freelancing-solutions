from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django_countries.fields import CountryField


class AbstractRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Password confirmation',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Enter the same password as before, for verification.',
    )
    email_valid = RegexValidator(r'^.+@.+\..+$', message='Invalid email ID')
    username = forms.CharField(help_text="Enter your email ID", validators=[email_valid])
    mobile_num_valid = RegexValidator(r'^\+?1?\d{9,15}$', message='Invalid mobile number.')
    mobile = forms.CharField(max_length=15, validators=[mobile_num_valid])
    description = forms.CharField(widget=forms.Textarea)
    address = forms.CharField(widget=forms.Textarea)
    country = CountryField().formfield(blank_label='(Select Country')

    class Meta:
        abstract = True

