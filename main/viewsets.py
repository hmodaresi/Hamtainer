from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend

from main.models import App, Container
from main.serializers import AppSerializer, ContainerSerializer


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer


class ContainerViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['app']
