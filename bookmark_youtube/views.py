from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark_youtube.models import BookmarkYoutube

# Create your views here.

class BookmarkYoutubeLV(ListView):
    model = BookmarkYoutube

class BookmarkYoutubeDV(DetailView):
    model = BookmarkYoutube