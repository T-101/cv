from django.db.models import Case, When
from rest_framework import viewsets

from cv.models import Employer, Employment, EmploymentTask
from cv.api_v1.serializers import EmployerSerializer, EmploymentTaskSerializer, EmploymentSerializer, PierSerializer


class EmployerViewSetContainer(viewsets.ModelViewSet):
    http_method_names = ('get',)


class EmployerViewSet(EmployerViewSetContainer):
    queryset = Employer.objects.filter(visible=True)
    serializer_class = EmployerSerializer


class EmploymentTaskViewSet(EmployerViewSetContainer):
    queryset = EmploymentTask.objects.order_by('sort_index')
    serializer_class = EmploymentTaskSerializer


class EmploymentViewSet(EmployerViewSetContainer):
    queryset = Employment.objects.filter(visible=True)
    serializer_class = EmploymentSerializer


class PierViewSet(EmployerViewSetContainer):

    def get_queryset(self):
        # Get Employer objects, sorted by foreign key
        ev = Employer.objects.filter(visible=True, employments__visible=True).order_by('-employments__date_start').values_list('pk')
        # Remove dupes while maintaining order
        """
        The following commented command gives wrong order in Python 3.5.3, but a correct order in 3.6.1
        """
        # l = [x[0] for x in list(dict.fromkeys(ev))]
        seen = set()
        unique_ids = [x[0] for x in ev if not (x[0] in seen or seen.add(x[0]))]

        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(unique_ids)])
        return Employer.objects.filter(pk__in=unique_ids).order_by(preserved)

    serializer_class = PierSerializer
