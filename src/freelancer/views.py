from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from accounts.models import Freelancer
from django.shortcuts import get_object_or_404


class FreelancerRequiredMixin(LoginRequiredMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, 'freelancer'):
            return super().dispatch(request, *args, **kwargs)
        else:
            return self.handle_no_permission()


class FreelancerDashboardView(FreelancerRequiredMixin, UpdateView):
    model = Freelancer
    fields = (
        'mobile',
        'description',
        'address',
        'country'
    )
    template_name = 'freelancer/dashboard.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Freelancer, user=self.request.user)
