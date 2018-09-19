from rest_framework import serializers

from info.models import PersonalInfo, NickName, ExternalLink, Email, PhoneNumber


class CVSerializer(serializers.HyperlinkedModelSerializer):
    def __init__(self, *args, **kwargs):
        exclude_fields = kwargs.pop('exclude_fields', None)
        super().__init__(*args, **kwargs)
        if exclude_fields:
            for item in exclude_fields:
                if item in self.fields:
                    self.fields.pop(item)


class PhoneNumberSerializer(CVSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'


class EmailSerializer(CVSerializer):
    class Meta:
        model = Email
        fields = '__all__'


class ExternalLinkSerializer(CVSerializer):
    class Meta:
        model = ExternalLink
        fields = '__all__'


class NicknameSerializer(CVSerializer):
    class Meta:
        model = NickName
        fields = '__all__'


class InfoSerializer(serializers.HyperlinkedModelSerializer):
    nick_names = NicknameSerializer(many=True, exclude_fields=['user'])
    phone_numbers = PhoneNumberSerializer(many=True, exclude_fields=['user'])
    emails = EmailSerializer(many=True, exclude_fields=['user'])
    external_links = ExternalLinkSerializer(many=True, exclude_fields=['user'])

    class Meta:
        model = PersonalInfo
        fields = '__all__'
