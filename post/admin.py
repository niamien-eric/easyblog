from django.contrib import admin
from post.models import Comment
from post.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_on", "last_updated")
    list_editable = ("published",)
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username','email','body')

admin.site.register(Comment, CommentAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
