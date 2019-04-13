from django.contrib import admin
from .models import Freelancer, Employer  # Import Freelancer and Employer modules


@admin.register(Freelancer)
class FreelancerAdmin(admin.ModelAdmin):
    """Register Freelancer module on the admin interface"""

    class Meta:
        model = Freelancer
        fields = '__all__'


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    """Register Employer module on the admin interface"""

    class Meta:
        model = Employer
        fields = '__all__'
