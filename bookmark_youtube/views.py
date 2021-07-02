from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark_youtube.models import BookmarkYoutube
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

class BookmarkYoutubeLV(ListView):
    model = BookmarkYoutube

class BookmarkYoutubeDV(DetailView):
    model = BookmarkYoutube

class BookmarkYoutubeCV(LoginRequiredMixin, CreateView):
    model = BookmarkYoutube
    fields = ['title', 'url']
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('bookmarkYoutube_index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookmarkYoutubeCV,self).form_valid(form)