from django.urls import path
from freelancer.views import DashboardView
from jobs.views import FreelancerBidListView

app_name = 'freelancer'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('bid-list', FreelancerBidListView.as_view(), name='bid-list')
]
