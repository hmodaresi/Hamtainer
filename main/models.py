from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
class App(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    command = models.CharField(max_length=150)
    env_vars = ArrayField()


class Container(models.Model):
    class ContainerStatus(models.TextChoices):
        RUNNING = 'R', 'Running'
        FINISHED = 'F', 'Finished'

    app = models.ForeignKey(App)
    status = models.CharField(max_length=1, choices=ContainerStatus, default=ContainerStatus.RUNNING)
    env_vars = ArrayField()
