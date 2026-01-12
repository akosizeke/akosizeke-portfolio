from django.db import migrations


def set_screenshot_images(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    updates = {
        "GovHire": "portfolio/projects/hire-6.png",
        "Face Recognition Attendance Monitoring": "portfolio/projects/face-4.png",
    }
    for title, image in updates.items():
        Project.objects.filter(title=title).update(image=image)


def undo_screenshot_images(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Project.objects.filter(
        title__in=[
            "GovHire",
            "Face Recognition Attendance Monitoring",
        ]
    ).update(image="")


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0009_seed_project_images"),
    ]

    operations = [
        migrations.RunPython(set_screenshot_images, reverse_code=undo_screenshot_images),
    ]
