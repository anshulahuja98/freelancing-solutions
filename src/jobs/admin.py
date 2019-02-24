from django.contrib import admin
from .models import Skill, Job, Bid  # Import Skill, Job, Bid module


# Register Skill module on the admin interface
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    class Meta:
        model = Skill
        # All fields of Skill
        fields = '__all__'


# Register Job module on the admin interface
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    class Meta:
        model = Job
        # All fields of Skill
        fields = '__all__'


# Register Bid module on the admin interface
@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    class Meta:
        model = Bid
        # All fields of Skill
        fields = '__all__'
