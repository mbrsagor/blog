from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'created_at']
    list_filter = ['title']
    list_editable = ['title']
    list_display_links = ['author']
    list_per_page = 2


admin.site.register(Post, PostAdmin)
