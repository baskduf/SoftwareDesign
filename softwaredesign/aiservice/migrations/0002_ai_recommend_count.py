# Generated by Django 5.0.6 on 2024-11-11 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aiservice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ai',
            name='recommend_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
