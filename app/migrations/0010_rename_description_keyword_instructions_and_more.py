# Generated by Django 4.2.7 on 2024-01-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_keyword_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keyword',
            old_name='description',
            new_name='instructions',
        ),
        migrations.AlterField(
            model_name='keyword',
            name='opis',
            field=models.TextField(default='SOME STRING'),
        ),
    ]
