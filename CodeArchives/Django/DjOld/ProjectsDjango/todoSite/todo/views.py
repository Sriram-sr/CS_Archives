from django.shortcuts import render,redirect
from .models import ToDo
from .forms import ToDoForm

def index(request):
    if request.method == "POST":
        form= ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')


    todo_list = ToDo.objects.all()
    form = ToDoForm()
    title = 'To-Do-List'
    context = {
        'list': todo_list,
        'form': form,
        'title': title
    }
    return render(request,"todo/index.html",context=context)

def delete(request,id):
    # if request.method=='POST':
    del_obj = ToDo.objects.get(id=id)
    del_obj.delete()
    return redirect('todo')