from django.urls import path
from freelancer.views import DashboardView

app_name = 'freelancer'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
