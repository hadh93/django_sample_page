from django.contrib import admin
from bookmark_youtube.models import BookmarkYoutube

# Register your models here.

class BookmarkYoutubeAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'create_date', 'modify_date')

admin.site.register(BookmarkYoutube, BookmarkYoutubeAdmin)