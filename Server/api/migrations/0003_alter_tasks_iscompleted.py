# Generated by Django 4.2.7 on 2023-11-29 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_categories_colors_icons_tasks_categories_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='isCompleted',
            field=models.BooleanField(default=False),
        ),
    ]
