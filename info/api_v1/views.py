from rest_framework import viewsets

from info.api_v1.serializers import InfoSerializer, NicknameSerializer, PhoneNumberSerializer, EmailSerializer, ExternalLinkSerializer
from info.models import PersonalInfo, NickName, PhoneNumber, Email, ExternalLink


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer


class PhoneNumberViewSet(viewsets.ModelViewSet):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer


class NicknameViewSet(viewsets.ModelViewSet):
    queryset = NickName.objects.all()
    serializer_class = NicknameSerializer


class InfoViewSet(viewsets.ModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = InfoSerializer

