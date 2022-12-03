from rest_framework import serializers

from main.models import App, Container


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'


class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = '__all__'
