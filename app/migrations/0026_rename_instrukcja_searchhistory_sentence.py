# Generated by Django 5.0.1 on 2024-01-27 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_rename_sentence_searchhistory_instrukcja'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searchhistory',
            old_name='instrukcja',
            new_name='sentence',
        ),
    ]
