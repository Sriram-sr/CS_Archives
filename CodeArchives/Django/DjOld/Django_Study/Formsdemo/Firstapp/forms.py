from django import forms

class EmployeeForm(forms.Form):
    name = forms.CharField()
    salary = forms.IntegerField()
    age = forms.IntegerField()
