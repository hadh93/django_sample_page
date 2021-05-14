from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class BookmarkIndexView(TemplateView):
    template_name = 'bookmark_index.html'
