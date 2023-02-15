# Generated by Django 4.1.4 on 2023-01-20 00:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Camera",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("camera_name", models.CharField(max_length=255)),
                (
                    "rtsp_camera",
                    models.CharField(
                        max_length=255,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Format must be rtsp:// [...]",
                                regex="(rtsp|rtmp):\\/\\/?([a-zA-Z0-9:@./_]*)",
                            )
                        ],
                    ),
                ),
                ("active", models.BooleanField(default=False)),
                ("alert_stolen_cars", models.BooleanField(default=False)),
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
