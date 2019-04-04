from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    # employer =
    class Meta:
        model = Job
        exclude = ('id',)
