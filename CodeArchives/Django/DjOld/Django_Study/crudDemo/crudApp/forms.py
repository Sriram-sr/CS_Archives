from django import forms
from crudApp import models
from crudApp.models import Student

class CreateForm(forms.ModelForm):
    # this class is created for retreiving data 
    class Meta:
        model = Student
        fields = '__all__'
        # exclude = ['sno']