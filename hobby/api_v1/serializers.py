from rest_framework import serializers

from hobby.models import HobbyItem, Hobby


class HobbyItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HobbyItem
        fields = '__all__'


class HobbySerializer(serializers.HyperlinkedModelSerializer):
    items = HobbyItemSerializer(many=True)

    class Meta:
        model = Hobby
        fields = '__all__'
