from rest_framework import serializers

from info.models import PersonalInfo


class InfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = ('real_name',)
