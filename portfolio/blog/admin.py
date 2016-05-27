from django.contrib import admin
from portfolio.blog.models import Entry, Tag


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    fields = ('headline', 'body', 'tags', 'published', 'preview')
    search_fields = ['headline', 'body', 'tags__name', 'published', 'preview']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fieds = ('name',)
    search_fields = ['name', 'created', 'updated']
