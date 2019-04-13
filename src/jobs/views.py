from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Job, Bid
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
        """Redirects to Employer's Job list page"""
        form.save()
        return HttpResponseRedirect(self.success_url)

    def post(self, request, *args, **kwargs):
        """Update the employer field with current user while submitting form"""
        self.request.POST._mutable = True
        self.request.POST.update({
            'employer': Employer.objects.get(user=self.request.user).id,
        })
        self.request.POST._mutable = False
        return super().post(request, args, kwargs)


class JobDetailView(FormMixin, DetailView, LoginRequiredMixin):
    model = Job
    template_name = 'jobs/job.html'
    context_object_name = 'job'
    form_class = BidForm
    success_url = '/jobs/freelancer'

    def get_object(self, queryset=None):
        return get_object_or_404(Job, id=self.kwargs.get('id'))

    def get_context_data(self, **kwargs):
        """Updates base template in context based on logged in user"""
        context = super(JobDetailView, self).get_context_data(**kwargs)
        if hasattr(self.request.user, 'employer'):
            context['base_template'] = 'employer/base.html'
        elif hasattr(self.request.user, 'freelancer'):
            context['base_template'] = 'freelancer/base.html'
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.request.POST._mutable = True
        self.request.POST.update({
            'job': self.get_object().id,
            'freelancer': Freelancer.objects.get(user=self.request.user).id,
        })
        self.request.POST._mutable = False
        return self.form_valid(form)

    def form_valid(self, form):
        form.save()
        return super(JobDetailView, self).form_valid(form)


class AbstractJobListView(LoginRequiredMixin, ListView):
    model = Job
    context_object_name = 'job_list'


class FreelancerJobListView(AbstractJobListView, FreelancerRequiredMixin):
    template_name = 'freelancer/job_list.html'

    def get_queryset(self):
        """Gets current freelancer user profile

        Returns:
            Job - Jobs bid by current freelancer
        """
        freelancer_user_profile = Freelancer.objects.get(user=self.request.user)
        return Job.objects.filter(skills_required__in=freelancer_user_profile.skills.all()).distinct()


class EmployerAddedJobListView(AbstractJobListView, EmployerRequiredMixin):
    template_name = 'employer/job_list.html'

    def get_queryset(self):
        """Gets current employer user profile

        Returns:
            Job - Jobs created by current employer
        """
        employer_user_profile = Employer.objects.get(user=self.request.user)
        return Job.objects.filter(employer=employer_user_profile)


class AbstractBidListView(LoginRequiredMixin, ListView):
    model = Bid
    context_object_name = 'bid_list'


class FreelancerBidListView(AbstractJobListView, FreelancerRequiredMixin):
    template_name = 'freelancer/bid_list.html'

    def get_queryset(self):
        freelancer_user_profile = Freelancer.objects.get(user=self.request.user)
        return Bid.objects.filter(freelancer=freelancer_user_profile)


class EmployerBidListView(AbstractJobListView, EmployerRequiredMixin):
    template_name = 'employer/bid_list.html'

    def get_queryset(self):
        employer_user_profile = Employer.objects.get(user=self.request.user)
        return Bid.objects.filter(employer=employer_user_profile)
