from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Job
from accounts.models import Freelancer


class JobListView(LoginRequiredMixin, ListView):
    model = Job
    context_object_name = 'job_list'
    template_name = 'main/job_list.html'

    def get_queryset(self):
        if hasattr(self.request.user, 'freelancer'):
            freelancer_user_profile = Freelancer.objects.get(user=self.request.user)
            return Job.objects.filter(skills_required__in=freelancer_user_profile.skills.all()).distinct()
        else:
            return None
