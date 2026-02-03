from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
class PostAbout(SummernoteModelAdmin):
     summernote_fields = ('title', 'content',)


# Register your models here.

