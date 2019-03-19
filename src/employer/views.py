from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from accounts.models import Employer
from django.shortcuts import get_object_or_404


class EmployerRequiredMixin(LoginRequiredMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, 'employer'):
            return super().dispatch(request, *args, **kwargs)
        else:
            return self.handle_no_permission()


class DashboardView(EmployerRequiredMixin, UpdateView):
    model = Employer
    fields = (
        'mobile',
        'description',
        'address',
        'country'
    )
    template_name = 'employer/dashboard.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Employer, user=self.request.user)
