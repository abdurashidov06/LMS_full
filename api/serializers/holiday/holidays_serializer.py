from rest_framework import serializers

from lms_apps.holidays.holidays import Holidays


class HolidaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holidays
        fields=('__all__',)
        read_only_fields=('id',)