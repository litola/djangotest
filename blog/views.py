from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
  posts = Blog.objects
  return render(request, 'blog/allblogs.html', {'posts':posts})

def post(request, blog_id):
  post = get_object_or_404(Blog, pk=blog_id)
  return render(request, 'blog/post.html', {'post':post})


# Create your views here.
