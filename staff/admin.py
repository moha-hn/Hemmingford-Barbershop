from django.contrib import admin
from .models import StaffMember, StaffPhoto, StaffVideo


class StaffPhotoInline(admin.TabularInline):
    model = StaffPhoto
    extra = 1


class StaffVideoInline(admin.TabularInline):
    model = StaffVideo
    extra = 1


@admin.register(StaffMember)
class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "is_active", "order")
    list_filter = ("role", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("name",)
    inlines = [StaffPhotoInline, StaffVideoInline]