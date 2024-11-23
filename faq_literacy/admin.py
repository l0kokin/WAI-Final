from django.contrib import admin
from .models import LiteracyCard


@admin.register(LiteracyCard)
class LiteracyCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview', 'link')

    def image_preview(self, obj):
        if obj.image_url:
            return obj.image_url
        return "No Image"

    image_preview.allow_tags = True
    image_preview.short_description = "Image"
