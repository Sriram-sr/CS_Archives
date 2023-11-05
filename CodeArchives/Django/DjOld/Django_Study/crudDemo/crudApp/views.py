from django.shortcuts import render,redirect
from crudApp.forms import CreateForm
# Create your views here.

from crudApp.models import Student

def retreive_db_data(request):
    all_data = Student.objects.all()
    our_pick = all_data[4]
    print(our_pick.sname)
    return render(request,'crudapp/index.html',context={'students':all_data})

def show_form(request):
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')

    return render(request,'crudApp/create.html',{'form':form})

def delete(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/show')

def update(request,id):
    if request.method == 'POST':
        sno = request.POST['number']
        sname = request.POST['name']
        sclass = request.POST['class']
        saddress = request.POST['address']
        student = Student.objects.get(id=id)
        student.sno = sno
        student.sname = sname
        student.sclass = sclass
        student.saddress = saddress
        student.save()
        return redirect('/show')
    student = Student.objects.get(id=id)
    return render(request,"crudApp/update.html",{'student':student})

