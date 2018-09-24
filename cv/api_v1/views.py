from rest_framework import viewsets

from cv.models import Employer, Employment, EmploymentTask
from cv.api_v1.serializers import EmployerSerializer, EmploymentTaskSerializer, EmploymentSerializer, PierSerializer


class EmployerViewSetContainer(viewsets.ModelViewSet):
    http_method_names = ('get',)


class EmployerViewSet(EmployerViewSetContainer):
    queryset = Employer.objects.filter(visible=False)
    serializer_class = EmployerSerializer


class EmploymentTaskViewSet(EmployerViewSetContainer):
    queryset = EmploymentTask.objects.all()
    serializer_class = EmploymentTaskSerializer


class EmploymentViewSet(EmployerViewSetContainer):
    queryset = Employment.objects.all()
    serializer_class = EmploymentSerializer


class PierViewSet(EmployerViewSetContainer):
    queryset = Employer.objects\
        .filter(visible=True)\
        .order_by('-employments__date_start')
    serializer_class = PierSerializer
