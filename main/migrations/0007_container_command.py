# Generated by Django 4.1.3 on 2022-12-04 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_container_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='command',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
