from django.views.generic import CreateView
from .models import Freelancer, Employer
from .forms import FreelancerRegisterForm, EmployerRegisterForm
from django.contrib.auth.views import LoginView as DefaultLoginView


class LoginView(DefaultLoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        url = "dashboard/"
        return url


class FreelancerRegisterFormView(CreateView):
    model = Freelancer
    form_class = FreelancerRegisterForm
    template_name = 'accounts/freelancer-register.html'
    success_url = '/accounts/login/'

    def form_valid(self, form):
        user = form.save()
        self.create_profile(user, **form.cleaned_data)
        return super(FreelancerRegisterFormView, self).form_valid(form)

    @staticmethod
    def create_profile(user=None, **kwargs):
        # Creates a new UserProfile object after successful creation of User object
        userprofile = Freelancer.objects.create(user=user,
                                                mobile=kwargs['mobile'],
                                                description=kwargs['description'],
                                                address=kwargs['address'],
                                                country=kwargs['country'],
                                                # profile_image=kwargs['profile_image'],
                                                )
        userprofile.save()


class EmployerRegisterFormView(CreateView):
    model = Employer
    form_class = EmployerRegisterForm
    template_name = 'accounts/employer-register.html'
    success_url = '/accounts/login/'

    def form_valid(self, form):
        user = form.save()
        self.create_profile(user, **form.cleaned_data)
        return super(EmployerRegisterFormView, self).form_valid(form)

    @staticmethod
    def create_profile(user=None, **kwargs):
        # Creates a new UserProfile object after successful creation of User object
        userprofile = Employer.objects.create(user=user,
                                              mobile=kwargs['mobile'],
                                              description=kwargs['description'],
                                              address=kwargs['address'],
                                              country=kwargs['country'],
                                              # profile_image=kwargs['profile_image'],
                                              )
        userprofile.save()
