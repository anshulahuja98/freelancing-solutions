from django import forms
from .models import Job, Bid


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('id',)


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['job', 'freelancer', 'amount', 'description', 'additional_description']
