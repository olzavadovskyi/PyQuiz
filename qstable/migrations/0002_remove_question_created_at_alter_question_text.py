# Generated by Django 5.1.4 on 2025-01-14 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qstable', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=255),
        ),
    ]
