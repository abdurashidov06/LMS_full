from rest_framework import serializers

from lms_apps.news.news import NewsCategory, News


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ('__all__',)




class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('__all__',)