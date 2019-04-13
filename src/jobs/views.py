from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Job
from accounts.models import Freelancer, Employer
from freelancer.views import FreelancerRequiredMixin
from employer.views import EmployerRequiredMixin
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from .forms import JobForm, BidForm


class JobFormView(EmployerRequiredMixin, CreateView):
    form_class = JobForm
    template_name = 'jobs/form.html'
    success_url = '/jobs/employer'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

    def post(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        self.request.POST.update({
            'employer': Employer.objects.get(user=self.request.user).id,
        })
        self.request.POST._mutable = False
        return super().post(request, args, kwargs)


class JobDetailView(LoginRequiredMixin, DetailView):
    model = Job
    template_name = 'jobs/job.html'
    context_object_name = 'job'

    def get_object(self, queryset=None):
        return get_object_or_404(Job, id=self.kwargs.get('id'))

    def get_context_data(self, **kwargs):
        context = super(JobDetailView, self).get_context_data(**kwargs)
        if hasattr(self.request.user, 'employer'):
            context['base_template'] = 'employer/base.html'
        elif hasattr(self.request.user, 'freelancer'):
            context['base_template'] = 'freelancer/base.html'
            context['form'] = BidForm
        return context


class AbstractJobListView(LoginRequiredMixin, ListView):
    model = Job
    context_object_name = 'job_list'


class FreelancerJobListView(AbstractJobListView, FreelancerRequiredMixin):
    template_name = 'freelancer/job_list.html'

    def get_queryset(self):
        freelancer_user_profile = Freelancer.objects.get(user=self.request.user)
        return Job.objects.filter(skills_required__in=freelancer_user_profile.skills.all()).distinct()


class EmployerAddedJobListView(AbstractJobListView, EmployerRequiredMixin):
    template_name = 'employer/job_list.html'

    def get_queryset(self):
        employer_user_profile = Employer.objects.get(user=self.request.user)
        return Job.objects.filter(employer=employer_user_profile)
