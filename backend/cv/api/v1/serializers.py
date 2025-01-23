import sys

from django.conf import settings
from django.db.models import Max
from django import VERSION as DJANGO_VERSION

from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import __version__ as rest_framework_version

from gunicorn import version_info as gunicorn_version

from cv.helpers import lol_crypt
from cv.models import PersonalInfo, Email, PhoneNumber, DetailCategory, DetailItem, Picture, Employer, Employment, \
    EmploymentTask, Hobby, HobbyItem, ExternalLink


class EmailSerializer(ModelSerializer):
    class Meta:
        model = Email
        fields = ["primary", "address"]


class PhoneNumberSerializer(ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ["primary", "number", "fa_class"]


class DetailItemSerializer(ModelSerializer):
    class Meta:
        model = DetailItem
        fields = ["text", "sort_order"]


class DetailCategorySerializer(ModelSerializer):
    detail_items = DetailItemSerializer(many=True)

    class Meta:
        model = DetailCategory
        fields = ["name", "detail_items", "sort_order"]


class PictureSerializer(ModelSerializer):
    class Meta:
        model = Picture
        fields = ["picture"]


class EmploymentTaskSerializer(ModelSerializer):
    class Meta:
        model = EmploymentTask
        fields = '__all__'


class EmploymentSerializer(ModelSerializer):
    date_start = SerializerMethodField()
    date_end = SerializerMethodField()
    employment_tasks = EmploymentTaskSerializer(many=True)

    class Meta:
        model = Employment
        fields = '__all__'

    def get_date_start(self, obj):
        return obj.date_start.strftime(obj.date_start_display_resolution)

    def get_date_end(self, obj):
        if obj.date_end:
            return obj.date_end.strftime(obj.date_end_display_resolution)


class EmployerSerializer(ModelSerializer):
    employments = EmploymentSerializer(many=True)

    class Meta:
        model = Employer
        fields = '__all__'


class HobbyItemSerializer(ModelSerializer):
    class Meta:
        model = HobbyItem
        fields = '__all__'


class HobbySerializer(ModelSerializer):
    hobby_items = HobbyItemSerializer(many=True)

    class Meta:
        model = Hobby
        fields = '__all__'


class ExternalLinkSerializer(ModelSerializer):
    class Meta:
        model = ExternalLink
        fields = '__all__'


class PersonalInfoSerializer(ModelSerializer):
    emails = SerializerMethodField()
    phone_numbers = SerializerMethodField()
    detail_categories = DetailCategorySerializer(many=True)
    pictures = PictureSerializer(many=True)
    employers = SerializerMethodField()
    hobbies = HobbySerializer(many=True)
    external_links = ExternalLinkSerializer(many=True)
    versions = SerializerMethodField()

    class Meta:
        model = PersonalInfo
        fields = ["first_name", "last_name", "title", "emails", "phone_numbers", "detail_categories", "pictures",
                  "employers", "hobbies", "external_links", "versions"]

    def get_employers(self, obj):
        # Annotation to remove duplicate row when ordering via foreign key
        queryset = obj.employers.prefetch_related("employments", "employments__employment_tasks") \
            .annotate(date_order=Max("employments__date_start")).order_by("-date_order")
        serializer = EmployerSerializer(queryset, many=True)
        return serializer.data

    def get_emails(self, obj):
        serializer = EmailSerializer(obj.emails, many=True)
        for i in serializer.data:
            i["address"] = i["address"].translate(lol_crypt)
        return serializer.data

    def get_phone_numbers(self, obj):
        serializer = PhoneNumberSerializer(obj.phone_numbers, many=True)
        for i in serializer.data:
            i["number"] = i["number"].translate(lol_crypt)
        return serializer.data

    @staticmethod
    def get_versions(_obj):
        return {
            "python": sys.version.split(" ")[0],
            "django": '.'.join(map(str, list(DJANGO_VERSION[0:3]))),
            "rest_framework": rest_framework_version,
            "gunicorn": '.'.join(map(str, list(gunicorn_version[0:3]))),
        }
