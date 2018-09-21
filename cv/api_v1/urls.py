from django.urls import path, include
from rest_framework import routers

from cv.api_v1.views import EmployerViewSet, EmploymentViewSet, EmploymentTaskViewSet

router = routers.DefaultRouter()
router.register('employer', EmployerViewSet)
router.register('employments', EmploymentViewSet)
router.register('employment_tasks', EmploymentTaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
