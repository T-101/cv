from django.urls import path, include
from rest_framework import routers

from info.api_v1.views import InfoViewSet, NicknameViewSet, PhoneNumberViewSet, EmailViewSet, ExternalLinkViewSet, \
    DetailViewSet, DetailItemViewSet

router = routers.DefaultRouter()
router.register('info', InfoViewSet)
router.register('nicknames', NicknameViewSet)
router.register('phonenumbers', PhoneNumberViewSet)
router.register('emails', EmailViewSet)
router.register('externallinks', ExternalLinkViewSet)
router.register('details', DetailViewSet)
router.register('detailitems', DetailItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
