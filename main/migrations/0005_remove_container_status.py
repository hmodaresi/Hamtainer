# Generated by Django 4.1.3 on 2022-12-04 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_container_docker_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='container',
            name='status',
        ),
    ]