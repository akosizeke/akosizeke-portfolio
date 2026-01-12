from django.db import migrations


def add_preview_images(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    updates = {
        "GovHire": "portfolio/projects/govhire-preview.svg",
        "Face Recognition Attendance Monitoring": "portfolio/projects/face-recognition-preview.svg",
    }
    for title, image in updates.items():
        Project.objects.filter(title=title).update(image=image)


def remove_preview_images(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Project.objects.filter(
        title__in=[
            "GovHire",
            "Face Recognition Attendance Monitoring",
        ]
    ).update(image="")


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0008_project_image"),
    ]

    operations = [
        migrations.RunPython(add_preview_images, reverse_code=remove_preview_images),
    ]
