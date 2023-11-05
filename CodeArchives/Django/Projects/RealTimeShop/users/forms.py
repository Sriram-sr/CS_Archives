from django.forms import ModelForm
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','email', 'password1', 'password2']
