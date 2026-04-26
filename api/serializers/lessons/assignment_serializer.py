from rest_framework import serializers

from lms_apps.lessons.assignment import Assignment
from lms_apps.lessons.lessons import Lesson


class AssignmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields=(
            'id',
            'lesson',
            'name',
            'description',
            'due_date',
            'score',
        )
        read_only_fields=('id',)

class AssignmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields=(
            'lesson',
            'name',
            'description',
            'due_date',
            'score',
        )

class LessonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields=(
            'lesson',
            'name',
            'description',
            'due_date',
            'score',
        )