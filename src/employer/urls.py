from django.urls import path
from employer.views import DashboardView


app_name = 'employer'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
