from rest_framework.response import Response
from rest_framework.views import APIView
from tweetsbyhashtag.TwitterService import TwitterAPI

class TweetsByHashTagAPIView(APIView):
    def get(self, request):
        limit = int(request.query_params.get('limit', 30))
        hash_tag = request.query_params.get('hashtag')
        print(limit, hash_tag)
        res = TwitterAPI().get_tweets_by_hashtag(hash_tag, limit, tweets=[])
        return Response(res, status=200)

class TweetsByUserAPIView(APIView):
    def get(self, request):
        limit = int(request.query_params.get('limit', 30))
        if limit < 5:
            limit = 5
        user_name = request.query_params.get('username')
        res = TwitterAPI().get_tweets_by_username(user_name, limit, tweets=[])
        if res is None:
            return Response("Could not find user with username: {}".format(user_name), status=400)
        return Response(res, status=200)
