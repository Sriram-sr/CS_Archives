from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=50)
    password = forms.CharField(label="password", max_length=50)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username','email','password1','password2']