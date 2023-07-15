from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForms

# Create your views here.
def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts.html', {'posts':posts})


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'posts/post_detail.html', {'post':post})


def post_new(request):

    if request.method == 'POST':
        form = PostForms(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.auther = request.user
            myform.save()
            return redirect('posts')
    else:
        form = PostForms()

    return render(request, 'posts/post_new.html', {'form':form})


    
        

def post_edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = PostForms(request.POST, request.FILES, instance=post)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.auther = request.user
            myform.save()
            return redirect('posts')
    else:
        form = PostForms(instance=post)

    return render(request, 'posts/post_new.html', {'form':form})
    


def post_delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('posts')