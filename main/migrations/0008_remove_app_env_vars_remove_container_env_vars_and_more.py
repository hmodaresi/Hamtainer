# Generated by Django 4.1.3 on 2022-12-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_container_command'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='env_vars',
        ),
        migrations.RemoveField(
            model_name='container',
            name='env_vars',
        ),
        migrations.AddField(
            model_name='app',
            name='env',
            field=models.JSONField(blank=True, default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='container',
            name='env',
            field=models.JSONField(blank=True, default=' '),
            preserve_default=False,
        ),
    ]
