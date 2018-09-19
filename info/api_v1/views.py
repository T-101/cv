from rest_framework import viewsets

from info.api_v1.serializers import InfoSerializer, NicknameSerializer, PhoneNumberSerializer, EmailSerializer, ExternalLinkSerializer
from info.models import PersonalInfo, NickName, PhoneNumber, Email, ExternalLink


class InfoViewSetContainer(viewsets.ModelViewSet):
    http_method_names = ('get',)


class EmailViewSet(InfoViewSetContainer):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer


class PhoneNumberViewSet(InfoViewSetContainer):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer


class NicknameViewSet(InfoViewSetContainer):
    queryset = NickName.objects.all()
    serializer_class = NicknameSerializer


class InfoViewSet(InfoViewSetContainer):
    queryset = PersonalInfo.objects.all()
    serializer_class = InfoSerializer

