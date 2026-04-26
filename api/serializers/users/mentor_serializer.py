from rest_framework import serializers

from lms_apps.mentor.mentor import Mentor


class MentorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields=(
            'id',
            'user',
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

class MentorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields=(
            'user',
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
                raise serializers.ValidationError("Passport 9 belgidan iborat bo'lishi kerak!!")
            return value



class MentorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields=(
            'user',
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
                raise serializers.ValidationError("Passport 9 belgidan iborat bo'lishi kerak!!")
            return value