# Generated by Django 5.0 on 2023-12-25 04:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0007_alter_taskmodel_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taskmodel",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 12, 25, 4, 54, 14, 175273, tzinfo=datetime.timezone.utc
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
            field=models.ManyToManyField(blank=True, null=True, to="tasks.taskimages"),
        ),
    ]
