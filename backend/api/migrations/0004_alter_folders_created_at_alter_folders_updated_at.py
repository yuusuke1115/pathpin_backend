# Generated by Django 4.1 on 2024-05-18 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_create_at_folders_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folders',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='folders',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
