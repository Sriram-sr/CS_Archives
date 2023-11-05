from email.mime import image
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView

def store_file(file):
    with open('temp/newImg.jpg','wb+') as Destination:
        for chunck in file.chunks():
            Destination.write(chunck)

class CreteProfileView(CreateView):
    template_name = 'upload.html'
    model = UserProfile
    fields = '__all__'
    success_url = ""


'''
class CreteProfileView(View):
    def get(self,request):
        form = ProfileForm()
        return render(request,'upload.html',{'form':form})
        # return render(request,'upload.html')

    def post(self,request):
        submittedForm = ProfileForm(request.POST,request.FILES)
        if submittedForm.is_valid():
            img_instance = UserProfile(image=request.FILES['file'])
            img_instance.save()
            img_path = UserProfile.objects.all()[0].image.path
            print(img_path)
        return HttpResponseRedirect('')    
            # store_file(request.FILES['file'])
            # return HttpResponseRedirect('')    
        # else :
            # return Http404    
        # store_file(request.FILES['image'])
'''        
