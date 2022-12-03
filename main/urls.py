from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.viewsets import AppViewSet

router = DefaultRouter()
router.register(r'app', AppViewSet)

urlpatterns = [
    path('', include(router.urls))
]
