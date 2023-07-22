from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForms


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post


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



