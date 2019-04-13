from django.urls import path
from jobs.views import EmployerBidListView
from employer.views import EmployerDashboardView

app_name = 'employer'

urlpatterns = [
    path('bid-list', EmployerBidListView.as_view(), name='bid-list'),
    path('dashboard/', EmployerDashboardView.as_view(), name='dashboard'),
]
