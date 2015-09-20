from rest_framework import serializers
from spider.models import Photo

__author__ = 'mattlyzheng'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        field = ('id', 'url')