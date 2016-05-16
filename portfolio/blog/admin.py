from django.contrib import admin
from portfolio.blog.models import Entry, Tag


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    fields = ('headline', 'body', 'tags')
    search_fields = ['headline', 'body', 'tags__name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fieds = ('name',)
    search_fields = ['name', 'created', 'updated']
