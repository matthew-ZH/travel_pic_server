from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from spider import views

__author__ = 'mattlyzheng'

# photo_list = PhotoViewSet.as_view({
#     'get':'list'
# })
#
# urlpatterns = format_suffix_patterns([
#     url(r'^photos/$', photo_list, name='photo-list'),
#     url(r'spider/$', views.PhotoSpider.as_view())
# ])


urlpatterns=[
    url(r'^photos/$', views.PhotoList.as_view()),
    url(r'^spider/$', views.PhotoSpider.as_view())
]

