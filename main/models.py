from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class App(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    command = models.CharField(max_length=150)
    env_vars = ArrayField(base_field=models.CharField(max_length=100))


class Container(models.Model):
    class ContainerStatus(models.TextChoices):
        RUNNING = 'R', 'Running'
        FINISHED = 'F', 'Finished'

    app = models.ForeignKey(App, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=ContainerStatus.choices, default=ContainerStatus.RUNNING)
    env_vars = ArrayField(base_field=models.CharField(max_length=100))
