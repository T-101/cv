from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from info.api_v1.serializers import InfoSerializer, NicknameSerializer, PhoneNumberSerializer, EmailSerializer, \
    ExternalLinkSerializer, DetailSerializer, DetailItemSerializer, PictureSerializer
from info.models import PersonalInfo, NickName, PhoneNumber, Email, ExternalLink, Detail, DetailItem, Picture


class InfoViewSetContainer(viewsets.ModelViewSet):
    http_method_names = ('get',)


class EmailViewSet(InfoViewSetContainer):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer


class ExternalLinkViewSet(InfoViewSetContainer):
    queryset = ExternalLink.objects.all()
    serializer_class = ExternalLinkSerializer


class PhoneNumberViewSet(InfoViewSetContainer):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer


class NicknameViewSet(InfoViewSetContainer):
    queryset = NickName.objects.all()
    serializer_class = NicknameSerializer


class InfoViewSet(InfoViewSetContainer):
    queryset = PersonalInfo.objects.all()
    serializer_class = InfoSerializer

    @action(detail=False)
    def me(self, *args, **kwargs):
        me = self.queryset.first()
        if not me:
            raise ImproperlyConfigured('Please add personal infoes to database before using this CV')

        self.object = get_object_or_404(self.queryset.model, pk=me.pk)
        serializer = self.get_serializer(self.object)
        return Response(serializer.data)


class DetailItemViewSet(InfoViewSetContainer):
    queryset = DetailItem.objects.order_by('sort_order')
    serializer_class = DetailItemSerializer


class DetailViewSet(InfoViewSetContainer):
    queryset = Detail.objects.order_by('sort_order')
    serializer_class = DetailSerializer


class PictureViewSet(InfoViewSetContainer):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    @action(detail=False)
    def random(self, *args, **kwargs):
        self.object = Picture.objects.order_by('?').first()
        serializer = self.get_serializer(self.object)
        return Response(serializer.data)
