from django.db.models import Case, When
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

    def get_queryset(self):
        # Get Employer objects, sorted by foreign key
        ev = Employer.objects.order_by('-employments__date_start').values_list('pk')
        # Remove dupes while maintaining order
        l = [x[0] for x in list(dict.fromkeys(ev))]

        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(l)])
        return Employer.objects.filter(pk__in=l).order_by(preserved)

    serializer_class = PierSerializer
