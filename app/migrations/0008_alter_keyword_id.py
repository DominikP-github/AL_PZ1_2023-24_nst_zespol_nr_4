# Generated by Django 4.2.7 on 2024-01-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_keyword_opis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
