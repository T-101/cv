from rest_framework import viewsets

from info.api_v1.serializers import InfoSerializer
from info.models import PersonalInfo


class InfoViewSet(viewsets.ModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = InfoSerializer
