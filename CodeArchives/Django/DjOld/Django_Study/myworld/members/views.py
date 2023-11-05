from multiprocessing import context
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,redirect
from django.template import loader
from .models import Members
# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hello world</h1>')

    # template = loader.get_template('myfirst.html')
    # return HttpResponse(template.render())

    mymembers = Members.objects.all().values()
    # mymembers = Members.objects.values_list('firstname') 
    # print(mymembers)
    template = loader.get_template('User_show.html')
    # context = {'mymembers': mymembers}
    return HttpResponse(template.render({'mymembers':mymembers},request))

def fnameview(request):
    all_members = Members.objects.all().values()
    template = loader.get_template("fname_show.html")
    return HttpResponse(template.render({'allmembers':all_members},request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({},request))
    
def addrecord(request):
    fname = request.POST['first']
    lname = request.POST['last']
    member = Members(firstname=fname,lastname=lname)
    member.save()
    # after saving we are going to redirect to the last page where all user data shown and where is add button present
    #  so import httpResponseredirect
    return HttpResponseRedirect(reverse('index'))
    # return redirect('')

def delete(request,id):
    member = Members.objects.get(id=id)    
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request,id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {'mymember':mymember}
    return HttpResponse(template.render(context,request))

def updaterecord(request,id):
    fname = request.POST['first']
    lname = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = fname
    member.lastname = lname
    member.save()
    return HttpResponseRedirect(reverse('index'))

