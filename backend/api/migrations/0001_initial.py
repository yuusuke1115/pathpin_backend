# Generated by Django 4.1 on 2024-05-18 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('create_at', models.CharField(max_length=256)),
                ('updated_at', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=256)),
                ('image_url', models.CharField(max_length=256)),
                ('memo', models.CharField(max_length=256)),
                ('create_at', models.CharField(max_length=256)),
                ('updated_at', models.CharField(max_length=256)),
            ],
        ),
    ]
