from rest_framework import serializers

from lms_apps.lessons.lessons import LessonItem


class LessonItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonItem
        fields=(
            'id',
            'lesson',
            'content',
            'file',
            'video',
        )
        read_only_fields=('id',)

class LessonItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonItem
        fields=(
            'lesson',
            'content',
            'file',
            'video',

        )

class LessonItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonItem
        fields=(
            'lesson',
            'content',
            'file',
            'video',

        )