from cmath import log
from email import message
from django.shortcuts import redirect, render
from .models import Room,Topic,Message
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username)
        if user is not None:
            user_auth = authenticate(username=username,password=password)
            if user_auth is not None:
                login(request,user_auth)
                return redirect('home')
            else:
                return render(request,"base/login_register.html",{"msg":"Username Password Invalid"})   
        else:
            return redirect('login',{"msg":"Username Password Invalid"})            
    return render(request,"base/login_register.html",{'page': page})

def register_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')

    return render(request,"base/login_register.html",{'form': form})

def logout_page(request):
    logout(request)
    return redirect('home')

def userprofile(request):
    return render(request,"base/userprofile.html")    

def home(request):
    # q = request.GET.get('q') if request.GET.get('q') != None else ''
    # rooms = Room.objects.filter(topic__name__icontains=q) # this will return if q value is given manually like 'py'
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # rooms = Room.objects.filter(topic__name__icontains=q)
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) 
        # Q(host__icontains=q)
    )
    room_messages = Message.objects.filter(
        Q(room__name__icontains=q) |
        Q(room__topic__name__icontains=q)
        )

    rooms_count = rooms.count()
    if q == 'all':
        rooms = Room.objects.all()
        room_messages = Message.objects.all()
    # else:    
        # rooms = Room.objects.filter(topic__name=q)
        # rooms = Room 
    # room1 = rooms[0]
    # print(room1.host.last_login)
    topics = Topic.objects.all()
    # room_messages = Message.objects.all()
    context = {'rooms': rooms,'topics': topics,'count': rooms_count,'messages': room_messages}
    return render(request,'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)    
    messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()
    if request.method == "POST":
        # msg_body = request.POST['body']
        msg_body = request.POST.get('body')
        Message.objects.create(
            user=request.user,
            room=room,
            body = msg_body,
        )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)
    context={'room': room,'messages':messages,'participants':participants}
    return render(request,"base/room.html",context)    

@login_required(login_url='login')
# @login_required  # this will through error whereas the above will redirect to login_url
def createroom(request):
    if request.method == 'POST':
        # print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:        
        form = RoomForm()    
        context = {'form': form}

        return render(request,"base/create.html",context=context)

@login_required(login_url='login')
def updateroom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.user != room.host:
        return HttpResponse('<h1>You are not allowed to Update details of Room')
        
    if request.method == 'POST':
        room = RoomForm(request.POST,instance=room) 
        if room.is_valid():
            room.save()
            return redirect('home')

    return render(request,"base/update.html",{'form': form})

@login_required(login_url='login')
def deleteroom(request,pk):
    room = Room.objects.get(id=pk)  
    if request.method=='POST':
        room.delete()
        return redirect('home')
    return render(request,"base/delete.html",context={'room': room})

@login_required(login_url='login')
def delete_message(request,pk):
    message = Message.objects.get(id=pk)
    if request.method == "POST":
        message.delete()
        deletemsg_room = message.room.id
        return redirect('room',pk=deletemsg_room)
        # return redirect(request.META['HTTP_REFERER'])
    return render(request,"base/delete.html",{'room':message})
    
    # message.delete()
    # if request.user == message.user:
    #     message.delete()
    #     return redirect('room',pk=deletemsg_room)
    # else:
    #     return HttpResponse('<h1>You are not allowed to delete this message')