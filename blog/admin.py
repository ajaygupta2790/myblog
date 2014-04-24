from django.contrib import admin
from blog.models import Post,Comment,Travel
# Register your models here.
search_fields = ['Comment']
admin.site.register(Post);
admin.site.register(Comment);
admin.site.register(Travel);