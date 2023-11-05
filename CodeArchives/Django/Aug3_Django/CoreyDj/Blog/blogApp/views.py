from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .models import Post
from .forms import PostForm

@login_required(login_url='login')
def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blogApp/home.html', context)

# the same above view can be written in class based view (ListView)

class PostListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Post
    template_name = 'blogApp/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post
    }

    return render(request, 'blogApp/post_detail.html', context)

# the same for viewing post in class based view 
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

def create_post(request):
    form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'blogApp/create-post.html', context)

# same above view in cbv
class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required(login_url='login')
def about(request):
    return render(request, 'blogApp/about.html')
