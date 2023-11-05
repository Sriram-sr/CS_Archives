from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('first', TemplateView.as_view(template_name='base/first.html', extra_context={'title': 'template view'}), name='first'),
]