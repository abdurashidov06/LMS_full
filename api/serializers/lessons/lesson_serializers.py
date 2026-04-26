from rest_framework import serializers

from lms_apps.lessons.lessons import Lesson


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields=(
            'id',
            'course',
            'name',
            'order',
        )
        read_only_fields=('id',)

class LessonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields=(
            'course',
            'name',
            'order',
        )

        def validate_order(self, value):
            if value < 0:
                raise serializers.ValidationError("Tartib raqami (order) manfiy bo'lishi mumkin emas.")

class LessonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields=(
            'course',
            'name',
            'order',
        )
