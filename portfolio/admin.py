from django.contrib import admin
from portfolio.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('headline', 'body', 'published')
