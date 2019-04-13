from django.urls import path
from employer.views import DashboardView
from jobs.views import EmployerBidListView

app_name = 'employer'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('bid-list', EmployerBidListView.as_view(), name='bid-list')
]
