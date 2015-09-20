# Create your views here.
import re
import urllib.request
from rest_framework import status
from rest_framework import generics

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from spider.models import Photo
from spider.serializers import PhotoSerializer
from spider.spider import getHtml, getImg


class PhotoList(APIView):
    def get(self, request, format=None):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)


class PhotoSpider(APIView):
    def get(self, request, format=None):
        html = getHtml("http://lvyou.baidu.com/pictravel/1fe4e438d02efe20d7b53735")
        imglist = getImg(html)
        Photo.objects.all().delete()
        for item in imglist:
            id = hash(item)
            photo = Photo(id=id, url=item)
            print(photo.url)
            photo.save()
        return Response(status=status.HTTP_200_OK)
