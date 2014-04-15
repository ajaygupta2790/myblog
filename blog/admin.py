from django.contrib import admin
from blog.models import Post,Comment
# Register your models here.
search_fields = ['Comment']
admin.site.register(Post);
admin.site.register(Comment);