from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Job
from accounts.models import Freelancer, Employer
from freelancer.views import FreelancerRequiredMixin
from employer.views import EmployerRequiredMixin
from django.shortcuts import get_object_or_404


class JobDetailView(LoginRequiredMixin, DetailView):
    model = Job
    template_name = 'jobs/job.html'
    context_object_name = 'job'

    def get_object(self, queryset=None):
        return get_object_or_404(Job, id=self.kwargs.get('id'))


class AbstractJobListView(LoginRequiredMixin, ListView):
    model = Job
    context_object_name = 'job_list'


class FreelancerJobListView(AbstractJobListView, FreelancerRequiredMixin):
    template_name = 'freelancer/job_list.html'

    def get_queryset(self):
        if hasattr(self.request.user, 'freelancer'):
            freelancer_user_profile = Freelancer.objects.get(user=self.request.user)
            return Job.objects.filter(skills_required__in=freelancer_user_profile.skills.all()).distinct()
        else:
            return None


class EmployerAddedJobListView(AbstractJobListView, EmployerRequiredMixin):
    template_name = 'employer/job_list.html'

    def get_queryset(self):
        if hasattr(self.request.user, 'employer'):
            employer_user_profile = Employer.objects.get(user=self.request.user)
            return Job.objects.filter(employer=employer_user_profile)
        else:
            return None
