from django.db import migrations


def replace_projects(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Project.objects.all().delete()
    Project.objects.bulk_create(
        [
            Project(
                title="GovHire",
                description="Portal para sa mabilis na paghanap at pag-post ng government job openings.",
                live_url="#",
                repo_url="#",
                tech_stack="Django, Postgres, Tailwind",
                featured=True,
                sort_order=1,
            ),
            Project(
                title="Face Recognition Attendance Monitoring",
                description="Attendance system na gumagamit ng face recognition para sa mabilis na log-in.",
                live_url="#",
                repo_url="#",
                tech_stack="Python, OpenCV, Django",
                featured=False,
                sort_order=2,
            ),
        ]
    )


def undo_replace(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Project.objects.filter(
        title__in=[
            "GovHire",
            "Face Recognition Attendance Monitoring",
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_seed_initial_projects'),
    ]

    operations = [
        migrations.RunPython(replace_projects, reverse_code=undo_replace),
    ]
