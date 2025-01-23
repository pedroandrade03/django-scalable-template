from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    """
    Abstract base admin for all application models.
    """

    readonly_fields = ("created_at", "updated_at", "id")
