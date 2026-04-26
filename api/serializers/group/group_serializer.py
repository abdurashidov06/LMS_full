from rest_framework import serializers

from lms_apps.group.group import Group


class GroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields=(
            'id',
            'picture',
            'name',
            'course',
            'mentor',
            'support',
            'study_days',
            'start_date',
            'start_time',
            'end_time',
            'classroom',
            'language',
            'study_type',

        )
        read_only_fields=('id',)

class GroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields=(
            'picture',
            'name',
            'course',
            'mentor',
            'support',
            'study_days',
            'start_date',
            'start_time',
            'end_time',
            'classroom',
            'language',
            'study_type',
        )

class GroupUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields=(
            'picture',
            'name',
            'course',
            'mentor',
            'support',
            'study_days',
            'start_date',
            'start_time',
            'end_time',
            'classroom',
            'language',
            'study_type',
        )
        read_only_fields=('id',)


