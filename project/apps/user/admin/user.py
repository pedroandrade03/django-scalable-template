from django.contrib import admin
from core.admin import BaseAdmin
from user.models import User


@admin.register(User)
class UserAdmin(BaseAdmin):
    list_display = ["email", "username", "is_active", "is_staff"]
    search_fields = ["email"]
    list_filter = ["is_active", "is_staff"]
