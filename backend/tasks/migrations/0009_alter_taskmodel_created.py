# Generated by Django 5.0 on 2023-12-25 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0008_alter_taskmodel_created_remove_taskmodel_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taskmodel",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 12, 25, 17, 20, 49, 341882, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
