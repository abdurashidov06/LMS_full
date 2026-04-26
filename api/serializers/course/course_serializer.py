from rest_framework import serializers

from lms_apps.course.course import Course


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=(
            'id',
            'name',
            'academic_hours_lesson',
            'academic_hours_total',
            'price',
            'payment_type',
        )
        read_only_fields=('id',)


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=(
            'name',
            'academic_hours_lesson',
            'academic_hours_total',
            'price',
            'payment_type',
        )

        def validate_price(self, value):
            if value < 0:
                raise serializers.ValidationError("Narx manfiy bo'lishi mumkin emas!!")


class CourseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=(
            'name',
            'academic_hours_lesson',
            'academic_hours_total',
            'price',
            'payment_type',
        )




