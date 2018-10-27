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


class EmploymentTaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentTask
        fields = ('id', 'name', 'sort_index')


class EmploymentModelSerializer(serializers.ModelSerializer):
    employment_tasks = EmploymentTaskModelSerializer(many=True)
    date_start = serializers.SerializerMethodField(method_name='format_date_start')
    date_end = serializers.SerializerMethodField(method_name='format_date_end')

    def format_date_start(self, obj):
        return obj.date_start.strftime(obj.date_start_display_resolution)

    def format_date_end(self, obj):
        if obj.date_end:
            return obj.date_end.strftime(obj.date_end_display_resolution)

    class Meta:
        model = Employment
        fields = ('employment_tasks', 'date_start', 'date_end', 'employment_status')


class PierSerializer(serializers.ModelSerializer):
    employments = EmploymentModelSerializer(many=True)

    class Meta:
        model = Employer
        fields = ('id', 'employments', 'name', 'description', 'url')
