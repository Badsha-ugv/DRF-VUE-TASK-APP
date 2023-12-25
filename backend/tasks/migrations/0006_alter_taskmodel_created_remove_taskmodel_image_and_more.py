# Generated by Django 5.0 on 2023-12-25 04:46

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0005_taskimages_alter_taskmodel_created_taskmodel_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taskmodel",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 12, 25, 4, 46, 58, 589583, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.RemoveField(
            model_name="taskmodel",
            name="image",
        ),
        migrations.AddField(
            model_name="taskmodel",
            name="image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="tasks.taskimages",
            ),
        ),
    ]
