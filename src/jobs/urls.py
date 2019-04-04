from django.urls import path
from .views import EmployerAddedJobListView, FreelancerJobListView, JobDetailView

app_name = 'jobs'

urlpatterns = [
    path('job/<uuid:id>/', JobDetailView.as_view(), name="job-detail"),
    path('employer/', EmployerAddedJobListView.as_view(), name='employer-job-list'),
    path('freelancer/', FreelancerJobListView.as_view(), name='freelancer-job-list'),
]
