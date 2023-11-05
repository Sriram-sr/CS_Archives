from pyexpat import model
from django import forms
from .models import Review
# class ReadyForm(forms.Form):
#     Username = forms.CharField(label="your name",max_length=100,error_messages={"required":"must not be empty","max_length":"Enter shorter name"})
#     place = forms.CharField(max_length=100)
#     password = forms.CharField(max_length=50)

class ReviewForm(forms.ModelForm):
    class Meta :
        model = Review
        fields = '__all__'
        # exclude = ['place',]
        labels = {
            "Username" : "Your name",
            "place" : "Your place",
            "Password" : "Your Password"
        }

        error_messages = {
            "Username" : {
               "required":"must not be empty",
               "max_length":"Enter shorter name" 
            }
        }
