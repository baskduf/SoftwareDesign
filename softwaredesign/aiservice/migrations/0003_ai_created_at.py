# Generated by Django 5.0.6 on 2024-11-11 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aiservice', '0002_ai_recommend_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='ai',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2024-01-01 00:00:00'),
            preserve_default=False,
        ),
    ]