from django.contrib import admin

# Register your models here.

from .models import Post 
from .models import BlogPost


admin.site.register(Post)
admin.site.register(BlogPost)