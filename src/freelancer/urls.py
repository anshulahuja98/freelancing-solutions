from django.urls import path
from django.views.generic import TemplateView

app_name = 'freelancer'

urlpatterns = [
    path('dashboard/', TemplateView.as_view(template_name='freelancer/dashboard.html'), name='dashboard'),
]
