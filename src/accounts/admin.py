from django.contrib import admin
from .models import Freelancer, Employer

# Register your models here.

@admin.register(Freelancer)
class FreelancerAdmin(admin.ModelAdmin):
    class Meta:
        model = Freelancer
        fields = '__all__'

