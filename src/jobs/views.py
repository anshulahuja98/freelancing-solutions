from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Job


class JobListView(LoginRequiredMixin, ListView):
    model = Job
    context_object_name = 'job_list'
    template_name = 'main/job_list.html'
