from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    live_url = models.URLField(blank=True)
    repo_url = models.URLField(blank=True)
    tech_stack = models.CharField(max_length=200, blank=True)
    featured = models.BooleanField(default=False)
    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-featured", "sort_order", "-created_at", "title"]

    def __str__(self):
        return self.title
