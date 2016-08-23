from django.contrib import admin
from portfolio.models import Post, Photo

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('headline', 'body')


admin.site.register(Photo)
