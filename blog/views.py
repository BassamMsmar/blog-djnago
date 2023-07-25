from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForms, CommentForm


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

class PostList(ListView):
    model = Post

# class PostDetail(DetailView):
#     model = Post


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)

    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.post = post
            myform.save()
    else:
        form = CommentForm()

        
    return render(request, 'blog/post_detail.html', {'post':post, 'comments':comments, 'form':form})


class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/blog'


class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    success_url = '/blog'



class PostDelete(DeleteView):
    model = Post
    fields = '__all__'
    success_url = '/blog'



