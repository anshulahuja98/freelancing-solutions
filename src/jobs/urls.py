from django.urls import path
from .views import EmployerAddedJobListView, FreelancerJobListView

app_name = 'jobs'

urlpatterns = [
    path('employer/', EmployerAddedJobListView.as_view(), name='employer-job-list'),
    path('freelancer/', FreelancerJobListView.as_view(), name='freelancer-job-list'),
]
