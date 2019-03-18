from django.contrib import admin
from .models import Freelancer, Employer  # Import Freelancer and Employer modules


# Register Freelancer module on the admin interface
@admin.register(Freelancer)
class FreelancerAdmin(admin.ModelAdmin):
    class Meta:
        model = Freelancer
        # All fields of Freelancer
        fields = '__all__'


# Register Employer module on the admin interface
@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    class Meta:
        model = Employer
        # All fields of Employer
        fields = '__all__'
