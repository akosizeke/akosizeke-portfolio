from django.db import migrations


def set_live_urls(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    updates = {
        "GovHire": "https://govhire-updated.onrender.com/",
        "Face Recognition Attendance Monitoring": "https://face-recognition-live-attendance.onrender.com/",
    }
    for title, url in updates.items():
        Project.objects.filter(title=title).update(live_url=url)


def reset_live_urls(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    defaults = {
        "GovHire": "https://govhire.example.com",
        "Face Recognition Attendance Monitoring": "https://fr-attendance.example.com",
    }
    for title, url in defaults.items():
        Project.objects.filter(title=title).update(live_url=url)


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0006_english_project_descriptions"),
    ]

    operations = [
        migrations.RunPython(set_live_urls, reverse_code=reset_live_urls),
    ]
