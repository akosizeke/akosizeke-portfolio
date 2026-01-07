from django.db import migrations


def english_descriptions(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    updates = {
        "GovHire": "Portal for quickly finding and posting government job openings.",
        "Face Recognition Attendance Monitoring": "Attendance system that uses face recognition for fast log-ins.",
    }
    for title, desc in updates.items():
        Project.objects.filter(title=title).update(description=desc)


def rollback_descriptions(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    # Leave existing descriptions unchanged on rollback
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_update_face_recognition_repo'),
    ]

    operations = [
        migrations.RunPython(english_descriptions, reverse_code=rollback_descriptions),
    ]
