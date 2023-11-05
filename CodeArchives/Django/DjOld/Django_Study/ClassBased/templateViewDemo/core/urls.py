from django.urls import path
from django.views.generic import TemplateView,RedirectView
from .views import ShowTemplate

app_name = 'core'

urlpatterns = [
    path('ex1',TemplateView.as_view(template_name="core/index.html",extra_context={'title':'Custom Title'})),
    path('ex2',ShowTemplate.as_view(),name='ex2'),
    path('rdt',RedirectView.as_view(url="http://www.instagram.com"),name='custom_url'),
]