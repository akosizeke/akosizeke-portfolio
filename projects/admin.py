from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "sort_order", "live_url", "repo_url")
    list_filter = ("featured",)
    search_fields = ("title", "description", "tech_stack")
    ordering = ("-featured", "sort_order", "title")
