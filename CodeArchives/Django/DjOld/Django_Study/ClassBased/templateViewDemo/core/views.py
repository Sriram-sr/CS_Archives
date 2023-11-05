from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import AllProducts

class ShowTemplate(TemplateView):
    template_name = "core/ex2.html"

    def get_context_data(self):
        # context = super().get_context_data(**kwargs)
        context = {}
        context['allproducts'] = AllProducts.objects.all()
        return context
