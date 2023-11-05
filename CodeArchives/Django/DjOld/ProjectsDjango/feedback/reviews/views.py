from typing import List
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from reviews.models import Review
from django.views.generic.edit import FormView

# Create your views here.
class ReviewForm(FormView):
    form_class = ReviewForm
    template_name = "reviews/base.html"


class ReviewView(View):
    def get(self,request):
        form = ReviewForm()    
        return render(request,"reviews/base.html",{"form":form})

    def post(self,request):
        username = request.POST['Username']
        form = ReviewForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect("/tq") 

class ThankyouView(TemplateView):
    template_name = "reviews/thank.html"
  # if you want any dynamic context to pass the the below function
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Use_Key"] = "Hello template"
        return context

class ReviewList(ListView):
      template_name = "reviews/listtemp.html"   
      model = Review
      context_object_name = "anyname you access at template" # default object_list
      

def check(request):
    if request.method == 'POST':
        username = request.POST['Username']
        form = ReviewForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect("/tq")
            
    form = ReviewForm()    
    return render(request,"reviews/base.html",{"form":form})

def tq(request):
    return render(request,"reviews/thank.html")    