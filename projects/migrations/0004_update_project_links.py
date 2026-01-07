from django.db import migrations


def update_links(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    updates = {
        "GovHire": {
            "live_url": "https://govhire.example.com",
            "repo_url": "https://github.com/akosizeke/govhire",
        },
        "Face Recognition Attendance Monitoring": {
            "live_url": "https://fr-attendance.example.com",
            "repo_url": "https://github.com/akosizeke/face-recognition-attendance",
        },
    }
    for title, data in updates.items():
        Project.objects.filter(title=title).update(**data)


def undo_links(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Project.objects.filter(
        title__in=[
            "GovHire",
            "Face Recognition Attendance Monitoring",
        ]
    ).update(live_url="#", repo_url="#")


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_replace_projects'),
    ]

    operations = [
        migrations.RunPython(update_links, reverse_code=undo_links),
    ]
