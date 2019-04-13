from django.views.generic import TemplateView
from django.shortcuts import redirect, reverse


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, 'employer'):
            return redirect(reverse('employer:dashboard'))
        elif hasattr(request.user, 'freelancer'):
            return redirect(reverse('freelancer:dashboard'))
        else:
            return super().dispatch(request, *args, **kwargs)
