# Generated by Django 4.1.3 on 2022-12-04 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_app_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='docker_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
