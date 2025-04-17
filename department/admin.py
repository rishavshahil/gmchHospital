from django.contrib import admin
from django.utils.html import format_html
from .models import HospitalDepartment, Doctor, OPD_Schedule
from unfold.admin import ModelAdmin

@admin.register(HospitalDepartment)
class DepartmentAdmin(ModelAdmin):
    list_display = ('Thumbnail', 'name', 'slug', 'order')
    readonly_fields = ('Thumbnail',)
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('order',)

    def Thumbnail(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 5px; object-fit: cover; object-position:top;" />', obj.thumbnail.url)
        return format_html('<span style="color: gray;">No Thumbnail</span>')

    Thumbnail.short_description = 'Thumbnail'

@admin.register(Doctor)
class DoctorAdmin(ModelAdmin):
    list_display = ('name', 'department', 'designation', 'registration_number')
    search_fields = ('name', 'designation', 'registration_number')
    list_filter = ('department',)

@admin.register(OPD_Schedule)
class OPDScheduleAdmin(ModelAdmin):
    list_display = ('department', 'doctor', 'room_no', 'visiting_days', 'order')
    list_filter = ('department', 'doctor')
    search_fields = ('room_no', 'visiting_days', 'department__name', 'doctor__name')
    ordering = ('order',)
