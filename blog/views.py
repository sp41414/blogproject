from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, SignupForm
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required 
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return redirect('blog:post_detail', post_id=post.id)  
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        return redirect("blog:post_detail", post_id=post.id) 
    if request.method == "POST":
        post.delete()
        return redirect("blog:home")
    return render(request, "blog/delete_post.html", {"post": post})

def home(request):
    posts = Post.objects.all().order_by("-created_at")
    print("Posts in DB:", posts)
    return render(request, "blog/home.html", {"posts": posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/post_detail.html", {"post": post})

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            if User.objects.filter(username=username).exists():
                messages.error(request, 'this user is already taken, choose another')
            else:
                user = form.save()
                login(request, user)
                return redirect("blog:home")
    else:
        form = SignupForm()
    return render(request, "blog/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("blog:home")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("blog:home")

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect("blog:home")
    else:
        form = PostForm()
    return render(request, "blog/create_post.html", {"form": form})
