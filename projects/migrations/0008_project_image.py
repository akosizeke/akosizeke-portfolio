from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0007_update_live_urls_to_render"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="image",
            field=models.CharField(
                blank=True,
                max_length=255,
                help_text="Static path or full URL for preview.",
            ),
        ),
    ]
