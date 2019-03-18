from django.urls import path
from django.views.generic import TemplateView

app_name = 'employer'

urlpatterns = [
    path('dashboard/', TemplateView.as_view(template_name='employer/dashboard.html'), name='dashboard'),
]
