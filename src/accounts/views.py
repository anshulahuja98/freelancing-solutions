# from django.shortcuts import render
from django.contrib.auth.views import LoginView as DefaultLoginView


class LoginView(DefaultLoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        url = "dashboard/"
        return url

