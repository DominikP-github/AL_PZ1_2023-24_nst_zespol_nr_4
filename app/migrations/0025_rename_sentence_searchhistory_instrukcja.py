# Generated by Django 5.0.1 on 2024-01-27 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_rename_description_searchhistory_opis'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searchhistory',
            old_name='sentence',
            new_name='instrukcja',
        ),
    ]
