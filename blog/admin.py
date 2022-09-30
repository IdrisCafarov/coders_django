from django.contrib import admin
from blog.models import *

# Register your models here.

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['title','created_date','updated_date']

admin.site.register(Category)
admin.site.register(SubCategory)

