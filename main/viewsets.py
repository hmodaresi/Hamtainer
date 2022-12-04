from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from main.models import App, Container
from main.serializers import AppSerializer, ContainerSerializer


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer

    def perform_create(self, serializer):
        super().perform_create(serializer)
        serializer.instance.pull()

    @action(detail=True, methods=['POST'])
    def run(self, request, pk):
        app = self.get_object()
        app.run()
        return Response(data={'msg': "Let's run the app", }, status=200)


class ContainerViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['app']
