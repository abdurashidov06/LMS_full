from rest_framework import serializers

from lms_apps.location.locations import Region, District


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields=('__all__',)
        read_only_fields=('id',)



class DistrictListSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields=(
            'id',
            'region',
            'name',
            'latitude',
            'longitude',
        )

class DistrictCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields=(
            'region',
            'name',
            'latitude',
            'longitude',
        )


class DistrictUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields=(
            'region',
            'name',
            'latitude',
            'longitude',
        )