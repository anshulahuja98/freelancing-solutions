from django.urls import path
from .views import FreelancerRegisterFormView, EmployerRegisterFormView, LoginView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/freelancer/', FreelancerRegisterFormView.as_view(), name='freelancer-register'),
    path('register/employer/', EmployerRegisterFormView.as_view(), name='employer-register'),
]
