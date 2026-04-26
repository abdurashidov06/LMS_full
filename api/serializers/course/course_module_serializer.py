from rest_framework import serializers

from lms_apps.course.course import CourseModule


class CourseModuleListSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseModule
        fields=(
            'id',
            'course',
            'name',
            'order',

        )
        read_only_fields=('id','course',)

class CourseModuleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseModule
        fields=(
            'course',
            'name',
            'order',
        )

        def validate_order(self, value):
            if value < 0:
                raise serializers.ValidationError("Tartib raqami (order) manfiy bo'lishi mumkin emas.")
            return value



class CourseModuleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseModule
        fields=(
            'course',
            'name',
            'order',

        )
