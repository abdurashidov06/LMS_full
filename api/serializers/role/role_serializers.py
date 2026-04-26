from rest_framework import serializers

from lms_apps.role.role import RoleCategory, Role


class RoleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleCategory
        fields = ('__all__',)

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('__all__',)