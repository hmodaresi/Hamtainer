from django.db import models
from django.contrib.postgres.fields import ArrayField

from main.docker_client import docker_client


# Create your models here.
class App(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    command = models.CharField(max_length=150)
    env_vars = ArrayField(base_field=models.CharField(max_length=100))

    def pull(self):
        docker_client.images.pull(self.image)

    def run(self):
        container = docker_client.containers.run(self.image, command=self.command, detach=True)
        Container.objects.create(app=self, env_vars=self.env_vars, docker_id=container.id)


class Container(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    env_vars = ArrayField(base_field=models.CharField(max_length=100))
    docker_id = models.CharField(max_length=100, default='')

    @property
    def status(self):
        return docker_client.containers.get(self.docker_id).status
