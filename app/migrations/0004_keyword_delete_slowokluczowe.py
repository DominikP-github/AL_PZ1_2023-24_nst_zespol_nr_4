# Generated by Django 4.2.7 on 2024-01-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_slowokluczowe_delete_historia_delete_instrukcje'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='SlowoKluczowe',
        ),
    ]
