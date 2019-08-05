from django.contrib import admin
from .models.recentlyviewd import RecentlyViewd
from .models.bookmark import BookMark
from .models.post import Post

# Register your models here.

admin.register(BookMark)
admin.register(Post)
admin.register(RecentlyViewd)
