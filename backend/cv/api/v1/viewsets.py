from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from cv.api.v1.serializers import PersonalInfoSerializer
from cv.models import PersonalInfo


class PersonalInfoViewSet(ModelViewSet):
    serializer_class = PersonalInfoSerializer

    def list(self, request, *args, **kwargs):
        queryset = PersonalInfo.load()
        serializer = self.serializer_class(queryset, many=False)
        return Response(serializer.data, status=200)
