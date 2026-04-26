from rest_framework import serializers

from lms_apps.auditory.classroom import Auditory


class AuditorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditory
        fields = '__all__'