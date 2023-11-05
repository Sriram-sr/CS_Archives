from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from users.serializers import ProjectSerializer
from .forms import CustomUserCreationForm
from django.http import HttpResponse
from rest_framework import generics
from projects.models import Project
from django.contrib import messages
from .forms import LoginForm
from rest_framework.response import Response


def register(request):
    # register_form = UserCreationForm()
    register_form = CustomUserCreationForm()
    return render(request,"users/register.html",{'form': register_form})

def register_check(request):
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    return HttpResponse('<h1>Hope Its a succcess</h1>')


def user_home(request):
    return render(request,"users/profiles.html")

def login_page(request):
    global form
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        sending_context = {}
        sending_context['form'] = form
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            print("User does not exist")    
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "Username or password is incorrect")
            sending_context['incorrect'] = True
            return render(request,"users/login.html",sending_context)
    return render(request,"users/login.html",{'form': form})


# @login_required(login_url='login')
def login_func(request):
    if request.method == 'POST':
        sending_context = {}
        sending_context['form'] = form
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            print("User does not exist")    
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "Username or password is incorrect")
            sending_context['incorrect'] = True
            return render(request,"users/login.html",sending_context)

def logout_func(request):
    logout(request)
    return redirect('login')            

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def projectsView(request):
    print(request.user)
    projects=Project.objects.all()
    serializer=ProjectSerializer(projects,many=True)    
    
    return Response(serializer.data)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
# permission_classes = (IsAuthenticated,)
def singleProjectView(request,pk):
    project=Project.objects.get(id=pk)
    user = request.user.profile
    print(user)
    serializer=ProjectSerializer(project,many=False)

    return Response(serializer.data)