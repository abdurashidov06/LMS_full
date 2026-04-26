from rest_framework import serializers

from lms_apps.branch.branch import Branch


class BranchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields=(
            'id',
            'name',
            'region',
            'district',
            'location',
            'latitude',
            'longitude',
        )
        read_only_fields=('id',)


class BranchCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields=(
            'name',
            'region',
            'district',
            'location',
            'latitude',
            'longitude',
        )

class BranchUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields=(
            'name',
            'region',
            'district',
            'location',
            'latitude',
            'longitude',
        )


