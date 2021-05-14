from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

class PostLV(ListView):
    model = Post

class PostDV(DetailView):
    model = Post

class PostCV(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'image', 'description']
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('blog_index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PostCV,self).form_valid(form)
