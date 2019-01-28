from django.contrib import admin
from .models import Skill, Job, Bid


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    class Meta:
        model = Skill
        fields = '__all__'

