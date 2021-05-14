"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mysite.views import IndexView, UserCreateView, UserCreateDoneTV

from bookmark.views import BookmarkLV, BookmarkDV
from bookmark_youtube.views import BookmarkYoutubeLV, BookmarkYoutubeDV
from blog.views import PostLV, PostDV, PostCV
from bookmarkIndex.views import BookmarkIndexView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name = 'index'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),

    path('bookmark/', BookmarkIndexView.as_view(), name='bookmark_index'),
    path('bookmark/regular/', BookmarkLV.as_view(), name='bookmark_regular_index'),
    path('bookmark/regular/<int:pk>/', BookmarkDV.as_view(), name = 'detail'),
    path('bookmark/youtube/', BookmarkYoutubeLV.as_view(), name = 'bookmarkYoutube_index'),
    path('bookmark/youtube/<int:pk>/', BookmarkYoutubeDV.as_view(), name = 'bookmarkYoutube_detail'),
    path('blog/', PostLV.as_view(), name='blog_index'),
    path('blog/<int:pk>/', PostDV.as_view(), name='blog_detail'),
    path('blog/add/', PostCV.as_view(), name="blog_add"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
