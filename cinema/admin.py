from django.contrib import admin
from .models import Post, Comment, Movies, Cinema

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Movies)
admin.site.register(Cinema)