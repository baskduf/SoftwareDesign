# Generated by Django 5.0.6 on 2024-09-17 01:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aiservice", "0001_initial"),
        ("authentication", "0005_ai_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatlog",
            name="ai",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="chat_logs",
                to="aiservice.ai",
            ),
        ),
        migrations.AlterField(
            model_name="userai",
            name="ai",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="aiservice.ai"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="ainame",
            field=models.ManyToManyField(
                blank=True, related_name="users", to="aiservice.ai"
            ),
        ),
        migrations.DeleteModel(
            name="AI",
        ),
    ]
