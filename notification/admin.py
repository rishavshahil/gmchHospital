from django.contrib import admin
from django.utils.html import format_html
from .models import HospitalNotice, HospitalTender
from unfold.admin import ModelAdmin, TabularInline

@admin.register(HospitalTender)
class HospitalTenderAdmin(ModelAdmin):
    list_display = ('title', 'category', 'publishing_date', 'closing_date', 'document_preview')
    readonly_fields = ('document_preview',)
    search_fields = ('title', 'category')  # Add search fields
    list_filter = ('category',)  # Add filters

    def document_preview(self, obj):
        if obj.document:
            return format_html('<a href="{}" target="_blank">View Document</a>', obj.document.url)
        return '(No document)'
    document_preview.short_description = 'Document Preview'


@admin.register(HospitalNotice )
class HospitalNoticeAdmin(ModelAdmin):
    list_display = ('title', 'category', 'notice_date', 'document_preview')
    readonly_fields = ('document_preview',)
    search_fields = ('title', 'category')  # Add search fields
    list_filter = ('category',) # Add filters
    
    def document_preview(self, obj):
        if obj.document:
            return format_html('<a href="{}" target="_blank">View Document</a>', obj.document.url)
        return '(No document)'
    document_preview.short_description = 'Document Preview'