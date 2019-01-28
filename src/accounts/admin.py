from django.contrib import admin
from .models import Freelancer, Employer


@admin.register(Freelancer)
class FreelancerAdmin(admin.ModelAdmin):
    class Meta:
        model = Freelancer
        fields = '__all__'


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    class Meta:
        model = Employer
        fields = '__all__'
