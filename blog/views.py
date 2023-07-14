from django.shortcuts import render
from .models import Post

# Create your views here.
def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts.html', {'posts':posts})


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'posts/post_detail.html', {'post':post})