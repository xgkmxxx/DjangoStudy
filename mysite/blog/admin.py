from django.contrib import admin

from .models import BlogsPost,Category,Tag
# Register your models here.

# class BlogPostAdmin(admin.ModelAdmin):
#     list_display = ('title','timestamp')

admin.site.register([BlogsPost,Category,Tag])