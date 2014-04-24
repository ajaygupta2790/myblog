from django.contrib import admin
from blog.models import Post,Comment,Travel
from django import forms
from ckeditor.widgets import CKEditorWidget

# Register your models here.

class TravelAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Travel

class TravelAdmin(admin.ModelAdmin):
    form = TravelAdminForm

search_fields = ['Comment']
admin.site.register(Post);
admin.site.register(Comment);
admin.site.register(Travel, TravelAdmin);