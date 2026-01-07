from django.db import migrations


def update_repo(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Project.objects.filter(
        title="Face Recognition Attendance Monitoring"
    ).update(
        repo_url="https://github.com/akosizeke/face-recognition-live-attendance-monitoring"
    )


def revert_repo(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Project.objects.filter(
        title="Face Recognition Attendance Monitoring"
    ).update(repo_url="#")


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_update_project_links'),
    ]

    operations = [
        migrations.RunPython(update_repo, reverse_code=revert_repo),
    ]
