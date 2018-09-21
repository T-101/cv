from rest_framework import serializers

from cv.models import Employer, Employment, EmploymentTask


class EmployerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'


class EmploymentSerializer(serializers.HyperlinkedModelSerializer):
    employer = EmployerSerializer(many=False)
    class Meta:
        model = Employment
        fields = '__all__'


class EmploymentTaskSerializer(serializers.HyperlinkedModelSerializer):
    employment = EmploymentSerializer(many=False)
    class Meta:
        model = EmploymentTask
        fields = '__all__'

