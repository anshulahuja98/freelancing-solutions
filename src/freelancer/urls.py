from jobs.views import FreelancerBidListView
from freelancer.views import FreelancerDashboardView
from django.urls import path

app_name = 'freelancer'

urlpatterns = [
    path('bid-list', FreelancerBidListView.as_view(), name='bid-list'),
    path('dashboard/', FreelancerDashboardView.as_view(), name='dashboard'),
]
