from django.contrib import admin
from .models import Skill, Job, Bid  # Import Skill, Job, Bid module


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Register Skill module on the admin interface"""
    class Meta:
        model = Skill
        fields = '__all__'


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    """Register Job module on the admin interface"""
    class Meta:
        model = Job
        fields = '__all__'


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    """Register Bid module on the admin interface"""
    class Meta:
        model = Bid
        fields = '__all__'
