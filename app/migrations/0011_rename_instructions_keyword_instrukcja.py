# Generated by Django 4.2.7 on 2024-01-07 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_description_keyword_instructions_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keyword',
            old_name='instructions',
            new_name='instrukcja',
        ),
    ]
