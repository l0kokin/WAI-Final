from django.contrib import admin
from .models import ResearchArticle


@admin.register(ResearchArticle)
class ResearchArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'url')
    search_fields = ('title', 'author')
    list_filter = ('author',)
    ordering = ('title',)
