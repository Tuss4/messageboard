from django.contrib import admin
from structure.models import Category, SubCategory, Topic, Post, PostCount

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(PostCount)
