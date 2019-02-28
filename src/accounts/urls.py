from django.urls import path
from .views import FreelancerRegisterFormView, EmployerRegisterFormView, LoginView
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('register/freelancer/', FreelancerRegisterFormView.as_view(), name='freelancer-register'),
    path('register/employer/', EmployerRegisterFormView.as_view(), name='employer-register'),
]
