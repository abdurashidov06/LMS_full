from rest_framework import serializers

from lms_apps.language.language import Language


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'