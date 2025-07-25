from django.contrib import admin
from apps.users import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    list_display = ("id", "username", "email", "get_full_name", "is_staff", "is_active", "created_at", "updated_at")
    list_display_links = ("id", "username")
    list_filter = ("is_staff", "is_active", "groups")
    search_fields = ("username", "email", "first_name", "last_name")
    readonly_fields = ("created_at", "updated_at", "created_by", "updated_by")
    
