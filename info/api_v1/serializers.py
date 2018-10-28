from rest_framework import serializers

from info.models import PersonalInfo, NickName, ExternalLink, Email, PhoneNumber, Detail, DetailItem, Picture


class CVSerializer(serializers.HyperlinkedModelSerializer):
    def __init__(self, *args, **kwargs):
        exclude_fields = kwargs.pop('exclude_fields', [])
        super().__init__(*args, **kwargs)
        for item in exclude_fields:
            self.fields.pop(item, None)


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


class DetailItemSerializer(CVSerializer):
    class Meta:
        model = DetailItem
        fields = '__all__'


class DetailSerializer(serializers.HyperlinkedModelSerializer):
    items = DetailItemSerializer(many=True, exclude_fields=['url', 'detail'])

    class Meta:
        model = Detail
        fields = '__all__'


class PictureSerializer(CVSerializer):

    class Meta:
        model = Picture
        fields = ['image']
