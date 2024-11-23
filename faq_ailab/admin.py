from django.contrib import admin
from .models import FaqAilab


class FaqAilabAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ('title', 'description')
    list_filter = ()


admin.site.register(FaqAilab, FaqAilabAdmin)
