## Python Twitter API

### Pre-requsites:
1. Python3.6 or higher
2. version control (git)

### Installation steps (assuming linux terminal):
```
1. git init
2. git clone https://github.com/gummadidala/tweets.git
3. cd tweets
4. cd twitter
5. pip install -r python-requirements.txt
6. python manage.py runserver 0:8002
```

### Usage:

1. #### Get tweets by a hashtag:
    **Endpoint URL** <br />
    ``` http://localhost:8002/twitter/api/byhashtag/ ``` <br />

    **Query Parameters** <br />
    _limit_ (integer) <br />
    _hashtag_ (string) (**with out #**) <br />

    **Example** <br />
    ``` curl "http://localhost:8002/twitter/api/byhashtag/?limit=20&hashtag=playbold" ``` <br />

2. #### Get user tweets:
    **Endpoint URL** <br />
    ``` http://localhost:8002/twitter/api/byuser/ ``` <br />

    **Query Parameters** <br />
    _limit_ (integer) <br />
    _username_ (string) <br />
    
    **Example** <br />
    ``` curl "http://localhost:8002/twitter/api/byuser/?limit=20&username=twitter" ``` <br />


