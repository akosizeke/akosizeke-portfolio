from django.shortcuts import render

from .models import Project


def list_projects(request):
    projects = Project.objects.order_by("-featured", "sort_order", "-created_at", "title")
    return render(request, "projects/list.html", {"projects": projects})
