from django.contrib import admin
from .models import Event, EventImage, EventVideo
from django.utils.html import format_html
from unfold.admin import ModelAdmin, TabularInline

class EventImageInline(TabularInline):
    model = EventImage
    extra = 1
    readonly_fields = ('image_preview',)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 200px; max-height: 200px; object-fit: cover; object-position:top;" />', obj.image.url)
        return '(No image)'
    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True

class EventVideoInline(TabularInline):
    model = EventVideo
    extra = 1
    readonly_fields = ('video_preview',)

    def video_preview(self, obj):
        if obj.video_file:
            return format_html('<video width="320" height="240" controls><source src="{}" type="video/mp4"></video>', obj.video_file.url)
        return '(No Video)'
    video_preview.short_description = 'Video Preview'
    video_preview.allow_tags = True

@admin.register(Event)
class EventAdmin(ModelAdmin):
    list_display = ('title', 'total_images', 'total_videos', 'created_at')
    readonly_fields = ('thumbnail_preview',)
    inlines = [EventImageInline, EventVideoInline]
    search_fields = ('title', 'description')

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" style="max-width: 200px; max-height: 200px; object-fit: cover; object-position:top;" />', obj.thumbnail.url)
        return '(No thumbnail)'
    
    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

    def total_images(self, obj):
        return obj.images.count()
    total_images.short_description = 'Total Images'

    def total_videos(self, obj):
        return obj.videos.count()
    total_videos.short_description = 'Total Videos'
