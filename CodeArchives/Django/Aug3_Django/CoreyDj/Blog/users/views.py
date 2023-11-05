from django.shortcuts import render, redirect
from .forms import CreateUserForm, UpdateUserForm, UpdateProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!!!')
            return redirect('login')
    form = CreateUserForm()
    context = {
        'form': form
    }

    return render(request, 'users/register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        wrong_user_flag = 0
        try:
            user = User.objects.get(username=username)
        except Exception as error:
            wrong_user_flag = 1
            messages.error(request, 'Enter a valid username')
        user = authenticate(request, username=username, password=password)    
        if user is not None:
            messages.success(request, f'{user} logged in Successfully...')
            login(request, user)
            return redirect('home')
        else:
            if wrong_user_flag!=1:
                messages.error(request, 'Password is incorrect')  
    return render(request, 'users/login.html')    

def logout_user(request):
    logout(request)    
    return redirect('login')

def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=profile)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile Successfully updated...!!!')
            return redirect('profile')
    context = {
        'profile': profile,
        'u_form': user_form,
        'p_form': profile_form
    }

    return render(request, 'users/profile-edit.html', context)

def profile(request):
    profile = Profile.objects.get(user=request.user)
    user_form = UpdateUserForm(instance=request.user)
    context = {
        'profile': profile,
        'u_form': user_form,
    }

    return render(request, 'users/profile.html', context)