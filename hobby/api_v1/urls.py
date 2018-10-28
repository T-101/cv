from django.urls import path, include
from rest_framework import routers

from hobby.api_v1.views import HobbyItemViewSet, HobbyViewSet

router = routers.DefaultRouter()
router.register('hobbies', HobbyViewSet)
router.register('hobbyitems', HobbyItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
