from django.shortcuts import render
from .models import Post
from .models import BlogPost
from todo import views as todo_views



def home(request):
    context = {
        
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html' , context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# views.py

def home(request):
    posts = BlogPost.objects.filter(is_deleted=False)  # ✅ Only show non-deleted posts
    return render(request, 'blog/home.html', {'posts': posts})



