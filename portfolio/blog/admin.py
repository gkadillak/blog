from django.contrib import admin
from portfolio.blog.models import Entry, Tag

# Register your models here.
admin.site.register(Tag)


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    fields = ('headline', 'body', 'tags')
