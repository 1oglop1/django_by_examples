from django.contrib import admin
from .models import Post


# Register your models here.

# class PostAdmin(admin.AdminSite):
#   list_display = ('title', 'slug', 'author', 'date_published', 'status')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'date_published', 'status')
    list_filter = ('status', 'date_created', 'date_published', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = { 'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'date_published'
    ordering = ['status', 'date_published']


admin.site.register(Post, PostAdmin)
