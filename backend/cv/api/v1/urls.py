from rest_framework.routers import SimpleRouter

from cv.api.v1.viewsets import PersonalInfoViewSet

router = SimpleRouter()

router.register('me', PersonalInfoViewSet, basename="me")
