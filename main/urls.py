from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.viewsets import AppViewSet, ContainerViewSet

router = DefaultRouter()
router.register(r'app', AppViewSet)
router.register(r'container', ContainerViewSet)

urlpatterns = [
    path('', include(router.urls))
]
