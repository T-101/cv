from django.urls import path, include
from rest_framework import routers

from info.api_v1.views import InfoViewSet, NicknameViewSet, PhoneNumberViewSet, EmailViewSet

router = routers.DefaultRouter()
router.register('info', InfoViewSet)
router.register('nicknames', NicknameViewSet)
router.register('phonenumbers', PhoneNumberViewSet)
router.register('emails', EmailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
