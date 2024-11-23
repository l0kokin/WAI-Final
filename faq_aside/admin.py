from django.contrib import admin
from .models import FaqAside


@admin.register(FaqAside)
class FaqAsideAdmin(admin.ModelAdmin):
    list_display = ('title', 'img_url', 'link_url')
