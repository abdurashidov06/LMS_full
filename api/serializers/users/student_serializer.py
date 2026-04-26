from rest_framework import serializers

from lms_apps.student.student import Student


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=(
            'id',
            'user',
            'group',
            'image',
            'surname',
            'name',
            'fathers_name',
            'region',
            'district',
            'birthday',
            'gender',
            'passport',
            'phone_number',
            'extra_phone_number',
            'location',
            'is_active',
            'created_at'
        )
        read_only_fields=('id','created_at',)


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=(
            'user',
            'group',
            'image',
            'surname',
            'name',
            'fathers_name',
            'region',
            'district',
            'birthday',
            'gender',
            'passport',
            'phone_number',
            'extra_phone_number',
            'location',
            'is_active',
        )

        def validate_passport(self,value):
            if len(str(value)) != 9:
                raise serializers.ValidationError("Passport 9 ta belgidan iborat bo'lishi kerak!!!")


class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=(
            'user',
            'group',
            'image',
            'surname',
            'name',
            'fathers_name',
            'region',
            'district',
            'birthday',
            'gender',
            'passport',
            'phone_number',
            'extra_phone_number',
            'location',
            'is_active',
        )

        def validate_passport(self,value):
            if len(str(value)) != 9:
                raise serializers.ValidationError("Passport 9 ta belgidan iborat bo'lishi kerak!!!")