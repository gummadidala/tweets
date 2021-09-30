import requests
import os
import json
from django.conf import settings

slash = os.sep

class TwitterAPI:

    def __init__(self):
        try:
            config_file = os.getcwd()+slash+"config"+slash+"twitter.config.json"
            f = open(config_file)
        except Exception as e:
            config_file = settings.CONFIG_PATH+slash+"twitter.config.json"
            f = open(config_file)
        self.config = json.load(f)
        self.bearer_token = self.config.get("bearer_token")

    def get_tweets_by_hashtag(self, hash_tag, limit, retry_count=0, tweets=[], next_results_url=None):
        try:
            self.hash_tag_url = self.config.get('tweets_by_hasgtag_api')
            req_headers={"Content-type":'application/json', "Authorization":"Bearer "+self.bearer_token}
            req_url = self.hash_tag_url + "?count={}&q=%23{}".format(limit, hash_tag)
            if next_results_url is not None:
                req_url = self.hash_tag_url + next_results_url
            # print(req_url)
            res = requests.get(req_url, headers = req_headers)
            if res.status_code == 200:
                results = res.json().get('statuses')
                tweets.extend(results)
                next_results_url = res.json().get("search_metadata").get('next_results')
                # maximum limit from twitter is 100
                if len(tweets) < limit and next_results_url:
                    self.get_tweets_by_hashtag(hash_tag, limit, retry_count, tweets, next_results_url)
            else:
                print("Some error happened with status code: {} and error message: {}".format(res.status_code, res.json().get('errors')))
            return tweets
        except requests.exceptions.RequestException as e:
            #Retry 3 times for connection errors
            if retry_count < 3:
                return self.get_tweets_by_hashtag(hash_tag, limit, retry_count+1)
        except Exception as e:
            print("In get_tweets_by_hashtag: {}".format(e))
    
    def get_tweets_by_username(self, user_name, limit, retry_count=0, tweets=[], next_token=None):
        try:
            user_id = self.get_userid_by_username(user_name)
            if user_id is None:
                return None
            tweets_by_user_api = self.config.get('tweets_by_user_api').format(user_id)
            req_url = tweets_by_user_api + "?max_results={}".format(limit)
            if next_token is not None:
                req_url += "pagination_token={}".format(next_token)
            req_headers={"Content-type":'application/json', "Authorization":"Bearer "+self.bearer_token}
            res = requests.get(req_url, headers = req_headers)
            if res.status_code == 200:
                results = res.json().get('data')
                tweets.extend(results)
                next_token = res.json().get("meta").get('next_token')
                # maximum limit from twitter is 100
                if len(tweets) < limit and next_token:
                    self.get_tweets_by_hashtag(user_name, limit, retry_count, tweets, next_token)
            else:
                print("Some error happened with status code: {} and error message: {}".format(res.status_code, res.json().get('errors')))
            return tweets
        except requests.exceptions.RequestException as e:
            #Retry 3 times for connection errors
            if retry_count < 3:
                return self.get_tweets_by_username(user_name, limit, retry_count+1)
        except Exception as e:
            print("In get_tweets_by_username: {}".format(e))
    
    def get_userid_by_username(self, user_name, retry_count=0):
        try:
            self.userid_url = self.config.get('userid_api').format(user_name)
            req_headers={"Content-type":'application/json', "Authorization":"Bearer "+self.bearer_token}
            res = requests.get(self.userid_url, headers=req_headers)
            if res.status_code == 200:
                try:
                    user_id = res.json().get('data')[0].get('id')
                except Exception as e:
                    return None
                return user_id
            else:
                print("Some error happened with status code: {} and error message: {}".format(res.status_code, res.json().get('errors')))
        except requests.exceptions.RequestException as e:
            #Retry 3 times for connection errors
            if retry_count < 3:
                return self.get_userid_by_username(user_name, retry_count+1)
        except Exception as e:
            print("In get_userid_by_username: {}".format(e))

if __name__=='__main__':
    t = TwitterAPI()
    res = t.get_tweets_by_hashtag("playbold", 5)