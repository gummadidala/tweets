from django.conf.urls import url
from tweetsbyhashtag.views import *
urlpatterns = [
    url(r'^api/byhashtag/$', TweetsByHashTagAPIView.as_view()),
    url(r'^api/byuser/$', TweetsByUserAPIView.as_view()),
]