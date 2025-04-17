from django.contrib import admin
from .models import Gallery, GalleryImage
from django.utils.html import format_html
from unfold.admin import ModelAdmin, TabularInline
from django.contrib.auth.models import Group
admin.site.unregister(Group) 

class ImageInline(TabularInline):
    model = GalleryImage
    extra = 1  # Number of empty forms to display
    # readonly_fields = ('image_preview',)

    # def image_preview(self, obj):
    #     if obj.image:
    #         return format_html('<img src="{}" style="max-width: 100px; max-height: 100px; object-fit: cover; object-position:top;" />', obj.image.url)
    #     return '(No image)'
    # image_preview.short_description = 'Image Preview'
    # image_preview.allow_tags = True


@admin.register(Gallery)
class GalleryAdmin(ModelAdmin):
    list_display = ('Thumbnail', 'title', 'total_images', 'created_at',)
    inlines = [ImageInline]
    
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title',)}

    def total_images(self, obj):
        return obj.images.count()
    
    def Thumbnail(self, obj):
        if obj.thumbnail:
            return format_html(f'<img src="{obj.thumbnail.url}" width="50" height="50" style="border-radius: 5px; object-fit: cover; object-position:top;" />', )
        return format_html('<span style="color: gray;">No Thumbnail</span>')

    Thumbnail.short_description = 'Thumbnail'
