# Generated by Django 3.2.19 on 2023-06-20 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_collection_id_download_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='download',
            name='timestamp',
        ),
    ]
