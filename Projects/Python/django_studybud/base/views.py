from django.shortcuts import redirect, render
from .models import Room,Topic,Message,Profile
from django.contrib.auth.models import User
from .forms import RoomForm,UserForm
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        print("login credentials receiveddddd")
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username)
        if user is not None:
            user_auth = authenticate(username=username,password=password)
            print("USreauth",user_auth)
            if user_auth is not None:
                login(request,user_auth)
                print("login success")
                return redirect('home')
            else:
                return render(request,"base/login_register.html",{"msg":"Username Password Invalid"})   
        else:
            return redirect('login',{"msg":"Username Password Invalid"})            
    return render(request,"base/login_register.html",{'page': page})

def register_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        username = request.POST['username']
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')

    return render(request,"base/signup.html",{'form': form})

def logout_page(request):
    logout(request)
    return redirect('home')

def userprofile(request,pk):
    user = User.objects.get(id=pk)
    profile = Profile.objects.get(user=user)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user,'rooms': rooms,'messages': room_messages,'topics': topics,'profile': profile}
    return render(request,"base/profile.html",context=context)    

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
    topics = topics[:3]
    # topics = {}
    # room_messages = Message.objects.all()
    # profile = Profile.objects.get(user=request.user)
    context = {'rooms': rooms,'topics': topics,'count': rooms_count,'messages': room_messages}#'profile':profile}
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
    topics = Topic.objects.all()
    if request.method == 'POST':
        # print(request.POST)
        topic_name = request.POST.get('topic')
        topic,created = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')
    else:        
        form = RoomForm()    
        context = {'form': form,'topics': topics}

        return render(request,"base/create-room.html",context=context)

@login_required(login_url='login')
def updateroom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    if request.user != room.host:
        return HttpResponse('<h1>You are not allowed to Update details of Room')
        
    if request.method == 'POST':
        # room = RoomForm(request.POST,instance=room) 
        # if room.is_valid():
        #     room.save()
        topic_name = request.POST.get('topic')
        topic,created = Topic.objects.get_or_create(name=topic_name)
        room.topic = topic
        room.name = request.POST.get('name')
        room.description = request.POST.get('description')
        room.save()

        return redirect('home')

    return render(request,"base/create-room.html",{'form': form,'topics': topics,'room': room})

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
    
@login_required(login_url='login')    
def updateprofile(request):
    form = UserForm()
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method == "POST":
        userform = UserForm(request.POST,instance=user)
        if userform.is_valid():
            userform.save()
            return redirect('user-profile',pk=user.id)
    return render(request,"base/updateProfile.html",context={'form': form,'profile': profile})    

def topicsList(request):
    try:
        q = request.GET['q']
    except:
        q = ''    
    topics = Topic.objects.filter(name__contains=q)
    context = {'topics': topics}
    return render(request,"base/topics.html",context=context)    