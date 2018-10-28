from rest_framework import viewsets

from hobby.models import Hobby, HobbyItem
from hobby.api_v1.serializers import HobbySerializer, HobbyItemSerializer


class HobbyViewSetContainer(viewsets.ModelViewSet):
    http_method_names = ('get',)


class HobbyViewSet(HobbyViewSetContainer):
    queryset = Hobby.objects.order_by('sort_order')
    serializer_class = HobbySerializer


class HobbyItemViewSet(HobbyViewSetContainer):
    queryset = HobbyItem.objects.order_by('sort_order')
    serializer_class = HobbyItemSerializer
