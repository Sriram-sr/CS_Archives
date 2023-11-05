from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.error_messages)    
    form = RegisterForm()
    context = {
        'form': form
    }

    return render(request, 'users/register.html', context=context)

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'users/login.html')

def home(request):
    return render(request, 'users/home.html')