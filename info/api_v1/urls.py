from django.urls import path, include
from rest_framework import routers

from info.api_v1.views import InfoViewSet

router = routers.DefaultRouter()
router.register('me', InfoViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
