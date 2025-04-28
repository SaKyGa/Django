from django.contrib import admin
from posts.models import Post, Category, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'updated_at', 'author']
    list_filter = ['category']
    search_fields = ['title', 'content']



admin.site.register(Category)
admin.site.register(Tag)

# Register your models here.
