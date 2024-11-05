from django.contrib import admin
from .models import DesignRequest

class DesignRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'category')
    list_filter = ('status', 'category')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('user', 'title', 'description', 'category', 'photo', 'admin_photo', 'status')
        }),
    )

admin.site.register(DesignRequest, DesignRequestAdmin)

