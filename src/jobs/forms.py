from django import forms
from .models import Job, Bid


class JobForm(forms.ModelForm):
    # employer =
    class Meta:
        model = Job
        exclude = ('id',)

