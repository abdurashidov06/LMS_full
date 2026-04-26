from rest_framework import serializers

from lms_apps.staff.staff import Staff


class StaffListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields=(
            'id',
            'user',
            'name',
            'position',
            'branch',
            'role',
            'image',
            'surname',
            'name',
            'father_name',
            'region',
            'district',
            'location',
            'birthday',
            'gender',
            'passport',
            'phone_number',
            'extra_phone_number',
            'is_active',
            'created_at',
        )
        read_only_fields=('id',)



class StaffCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields=(
            'user',
            'name',
            'position',
            'branch',
            'role',
            'image',
            'surname',
            'name',
            'father_name',
            'region',
            'district',
            'location',
            'birthday',
            'gender',
            'passport',
            'phone_number',
            'extra_phone_number',
            'is_active',
        )

        def validate_passport(self,value):
            if len(str(value)) != 9:
                raise serializers.ValidationError("Passport 9 belgidan iborat bo'lishi kerak!!")
            return value



class StaffUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields=(
            'user',
            'name',
            'position',
            'branch',
            'role',
            'image',
            'surname',
            'name',
            'father_name',
            'region',
            'district',
            'location',
            'birthday',
            'gender',
            'passport',
            'phone_number',
            'extra_phone_number',
            'is_active',
        )

        def validate_passport(self,value):
            if len(str(value)) != 9:
                raise serializers.ValidationError("Passport 9 belgidan iborat bo'lishi kerak!!")
            return value