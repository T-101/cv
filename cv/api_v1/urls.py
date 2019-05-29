from django.conf import settings
from django.urls import path, include
from rest_framework import routers

from cv.api_v1.views import EmployerViewSet, EmploymentViewSet, EmploymentTaskViewSet, PierViewSet

router = routers.DefaultRouter() if settings.DEBUG else routers.SimpleRouter()
router.register('employers', EmployerViewSet)
router.register('employments', EmploymentViewSet)
router.register('employment_tasks', EmploymentTaskViewSet)
router.register('pier', PierViewSet, base_name='pier')

urlpatterns = [
    path('', include(router.urls)),
]
