# Generated by Django 4.2 on 2023-06-08 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("TestApp", "0012_blogcomment"),
    ]

    operations = [
        migrations.RemoveField(model_name="blogcomment", name="parent",),
        migrations.CreateModel(
            name="subComment",
            fields=[
                ("sno", models.AutoField(primary_key=True, serialize=False)),
                ("comment", models.TextField()),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="TestApp.post"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]