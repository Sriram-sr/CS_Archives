from django.shortcuts import render
from .forms import ProjectForm
from .models import Project


def form(request):
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            print("_________________valid_____________________")
            form.save()

    form = ProjectForm()
    return render(request,"projects/form.html",{'form':form})

def projects(request):
    project = Project.objects.all()
    return render(request,"projects/project.html",{'projects': project})
