from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Post

def blog_home(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/blog_home.html', {'posts': posts})

def blog_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/blog_post.html', {'post': post})
