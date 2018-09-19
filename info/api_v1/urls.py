from django.urls import path, include
from rest_framework import routers

from info.api_v1.views import InfoViewSet, NicknameViewSet, PhoneNumberViewSet, EmailViewSet

router = routers.DefaultRouter()
router.register('me', InfoViewSet)
router.register('nicknames', NicknameViewSet)
router.register('phonenumbers', PhoneNumberViewSet)
router.register('emails', EmailViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
